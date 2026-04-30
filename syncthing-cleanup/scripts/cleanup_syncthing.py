#!/usr/bin/env python3
"""
Syncthing Cleanup Script

Removes unexpected items from Syncthing sync folders:
- Conflict files (.sync-conflict-*)
- Empty directories
- Temporary files (*.swp, *~, .DS_Store, etc.)
- Broken symlinks
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse


class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def color_print(message: str, color: str = Colors.WHITE, bold: bool = False) -> None:
    """Print colored message to terminal"""
    prefix = color
    if bold:
        prefix += Colors.BOLD
    print(f"{prefix}{message}{Colors.RESET}")


def print_header(message: str) -> None:
    """Print section header"""
    color_print(f"\n{'=' * 60}", Colors.CYAN)
    color_print(f"  {message}", Colors.CYAN, bold=True)
    color_print(f"{'=' * 60}\n", Colors.CYAN)


def print_success(message: str) -> None:
    """Print success message"""
    color_print(f"✓ {message}", Colors.GREEN)


def print_warning(message: str) -> None:
    """Print warning message"""
    color_print(f"⚠ {message}", Colors.YELLOW)


def print_error(message: str) -> None:
    """Print error message"""
    color_print(f"✗ {message}", Colors.RED)


def print_info(message: str) -> None:
    """Print info message"""
    color_print(f"ℹ {message}", Colors.BLUE)


class SyncthingConfig:
    """Parse and store Syncthing configuration"""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = self._find_config(config_path)
        self.api_key: Optional[str] = None
        self.gui_url: Optional[str] = None
        self.folders: Dict[str, str] = {}  # folder_id -> path
        self._parse_config()

    def _find_config(self, config_path: Optional[str]) -> Path:
        """Find Syncthing configuration file"""
        if config_path:
            return Path(config_path)

        # Common config locations
        possible_paths = [
            Path.home() / '.config' / 'syncthing' / 'config.xml',
            Path.home() / '.syncthing' / 'config.xml',
            Path.home() / 'Library' / 'Application Support' / 'Syncthing' / 'config.xml',
        ]

        for path in possible_paths:
            if path.exists():
                return path

        raise FileNotFoundError(
            "Could not find Syncthing configuration. "
            "Please specify with --config option."
        )

    def _parse_config(self) -> None:
        """Parse Syncthing config.xml"""
        try:
            with open(self.config_path, 'r') as f:
                content = f.read()

            # Extract API key
            api_key_match = re.search(r'<apikey>([^<]+)</apikey>', content)
            if api_key_match:
                self.api_key = api_key_match.group(1)

            # Extract GUI address
            gui_match = re.search(r'<address>([^<]+)</address>', content)
            if gui_match:
                self.gui_url = gui_match.group(1)

            # Extract folder paths
            folder_pattern = r'<folder[^>]*id="([^"]+)"[^>]*path="([^"]+)'
            for match in re.finditer(folder_pattern, content):
                folder_id, folder_path = match.groups()
                # Expand ~ in path
                expanded_path = Path(folder_path).expanduser()
                self.folders[folder_id] = str(expanded_path)

        except Exception as e:
            raise RuntimeError(f"Failed to parse config: {e}")

    def get_folder_paths(self) -> List[str]:
        """Get list of all sync folder paths"""
        return list(self.folders.values())

    def get_gui_url(self) -> str:
        """Get full GUI URL for API calls"""
        if not self.gui_url:
            raise RuntimeError("Could not find GUI address in config")

        # Add protocol if missing
        if not self.gui_url.startswith('http'):
            return f"http://{self.gui_url}"
        return self.gui_url


class CleanupScanner:
    """Scan for items to clean up"""

    def __init__(self, folders: List[str], verbose: bool = False):
        self.folders = folders
        self.verbose = verbose
        self.conflicts: List[Path] = []
        self.empty_dirs: List[Path] = []
        self.temp_files: List[Path] = []
        self.broken_symlinks: List[Path] = []

    def scan(self, types: Optional[Set[str]] = None) -> None:
        """Scan all folders for items to clean"""
        if types is None:
            types = {'conflicts', 'empty', 'temp', 'symlinks'}

        print_header("Scanning for unexpected items...")

        for folder in self.folders:
            if not Path(folder).exists():
                print_warning(f"Folder does not exist: {folder}")
                continue

            print_info(f"Scanning {folder}...")

            if 'conflicts' in types:
                self._scan_conflicts(folder)

            if 'empty' in types:
                self._scan_empty_dirs(folder)

            if 'temp' in types:
                self._scan_temp_files(folder)

            if 'symlinks' in types:
                self._scan_broken_symlinks(folder)

    def _scan_conflicts(self, folder: str) -> None:
        """Find conflict files"""
        try:
            path = Path(folder)
            conflicts = list(path.rglob("*.sync-conflict-*"))
            self.conflicts.extend(conflicts)

            if self.verbose and conflicts:
                print(f"  Found {len(conflicts)} conflict files")
        except Exception as e:
            print_error(f"Error scanning conflicts in {folder}: {e}")

    def _scan_empty_dirs(self, folder: str) -> None:
        """Find empty directories"""
        try:
            path = Path(folder)
            empty_dirs = []

            for root in path.rglob('*'):
                if root.is_dir():
                    try:
                        # Check if directory is empty
                        if not any(root.iterdir()):
                            empty_dirs.append(root)
                    except PermissionError:
                        pass

            self.empty_dirs.extend(empty_dirs)

            if self.verbose and empty_dirs:
                print(f"  Found {len(empty_dirs)} empty directories")
        except Exception as e:
            print_error(f"Error scanning empty dirs in {folder}: {e}")

    def _scan_temp_files(self, folder: str) -> None:
        """Find temporary files"""
        temp_patterns = [
            "*.swp", "*.swo",  # Vim swap files
            "*~",  # Backup files
            ".DS_Store",  # macOS
            "Thumbs.db",  # Windows
            "*.tmp",  # Generic temp files
            "*.bak",  # Backup files
        ]

        try:
            path = Path(folder)
            for pattern in temp_patterns:
                temp_files = list(path.rglob(pattern))
                self.temp_files.extend(temp_files)

            if self.verbose:
                print(f"  Found {len(self.temp_files)} temporary files")
        except Exception as e:
            print_error(f"Error scanning temp files in {folder}: {e}")

    def _scan_broken_symlinks(self, folder: str) -> None:
        """Find broken symbolic links"""
        try:
            path = Path(folder)
            broken = []

            for item in path.rglob('*'):
                if item.is_symlink():
                    try:
                        # Check if target exists
                        if not item.exists():
                            broken.append(item)
                    except (OSError, PermissionError):
                        broken.append(item)

            self.broken_symlinks.extend(broken)

            if self.verbose and broken:
                print(f"  Found {len(broken)} broken symlinks")
        except Exception as e:
            print_error(f"Error scanning symlinks in {folder}: {e}")

    def get_summary(self) -> Dict[str, int]:
        """Get summary of found items"""
        return {
            'conflicts': len(self.conflicts),
            'empty_dirs': len(self.empty_dirs),
            'temp_files': len(self.temp_files),
            'broken_symlinks': len(self.broken_symlinks),
            'total': (
                len(self.conflicts) +
                len(self.empty_dirs) +
                len(self.temp_files) +
                len(self.broken_symlinks)
            )
        }

    def print_results(self) -> None:
        """Print scan results"""
        summary = self.get_summary()

        print_header("Scan Results")

        print(f"  Conflict files:     {summary['conflicts']}")
        print(f"  Empty directories:  {summary['empty_dirs']}")
        print(f"  Temporary files:    {summary['temp_files']}")
        print(f"  Broken symlinks:    {summary['broken_symlinks']}")
        print(f"  {'─' * 40}")
        color_print(f"  Total items:        {summary['total']}", Colors.CYAN, bold=True)


class CleanupExecutor:
    """Execute cleanup operations"""

    def __init__(self, scanner: CleanupScanner, verbose: bool = False):
        self.scanner = scanner
        self.verbose = verbose
        self.deleted_conflicts = 0
        self.deleted_empty_dirs = 0
        self.deleted_temp_files = 0
        self.deleted_symlinks = 0
        self.errors: List[str] = []

    def execute(self) -> None:
        """Execute cleanup operations"""
        print_header("Cleaning up...")

        self._delete_conflicts()
        self._delete_empty_dirs()
        self._delete_temp_files()
        self._delete_symlinks()

        self._print_summary()

    def _delete_conflicts(self) -> None:
        """Delete conflict files"""
        for file in self.scanner.conflicts:
            try:
                file.unlink()
                self.deleted_conflicts += 1
                if self.verbose:
                    print(f"  Deleted: {file}")
            except Exception as e:
                self.errors.append(f"Failed to delete {file}: {e}")

    def _delete_empty_dirs(self) -> None:
        """Delete empty directories (sort by path length, delete deepest first)"""
        # Sort by path length descending to delete deepest directories first
        sorted_dirs = sorted(self.scanner.empty_dirs, key=lambda x: len(str(x)), reverse=True)

        for dir in sorted_dirs:
            try:
                dir.rmdir()
                self.deleted_empty_dirs += 1
                if self.verbose:
                    print(f"  Deleted: {dir}/")
            except Exception as e:
                self.errors.append(f"Failed to delete {dir}: {e}")

    def _delete_temp_files(self) -> None:
        """Delete temporary files"""
        for file in self.scanner.temp_files:
            try:
                file.unlink()
                self.deleted_temp_files += 1
                if self.verbose:
                    print(f"  Deleted: {file}")
            except Exception as e:
                self.errors.append(f"Failed to delete {file}: {e}")

    def _delete_symlinks(self) -> None:
        """Delete broken symlinks"""
        for link in self.scanner.broken_symlinks:
            try:
                link.unlink()
                self.deleted_symlinks += 1
                if self.verbose:
                    print(f"  Deleted: {link}")
            except Exception as e:
                self.errors.append(f"Failed to delete {link}: {e}")

    def _print_summary(self) -> None:
        """Print cleanup summary"""
        print_header("Cleanup Summary")

        print(f"  Conflict files deleted:     {self.deleted_conflicts}")
        print(f"  Empty directories deleted:  {self.deleted_empty_dirs}")
        print(f"  Temporary files deleted:    {self.deleted_temp_files}")
        print(f"  Broken symlinks deleted:    {self.deleted_symlinks}")
        print(f"  {'─' * 40}")

        total = (self.deleted_conflicts + self.deleted_empty_dirs +
                 self.deleted_temp_files + self.deleted_symlinks)

        if total > 0:
            color_print(f"  Total deleted:             {total}", Colors.GREEN, bold=True)
        else:
            color_print(f"  Total deleted:             {total}", Colors.YELLOW)

        if self.errors:
            print(f"\n{Colors.RED}Errors encountered:{Colors.RESET}")
            for error in self.errors[:10]:  # Show first 10 errors
                print(f"  • {error}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors) - 10} more errors")


class SyncthingAPI:
    """Interact with Syncthing REST API"""

    def __init__(self, config: SyncthingConfig):
        self.config = config
        self.api_key = config.api_key
        self.gui_url = config.get_gui_url()

    def trigger_rescan(self, folder_id: str) -> bool:
        """Trigger rescan for a specific folder"""
        try:
            url = f"{self.gui_url}/rest/db/scan?folder={folder_id}"
            result = subprocess.run(
                ['curl', '-s', '-X', 'POST', '-H', f'X-API-Key: {self.api_key}', url],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except Exception as e:
            print_error(f"Failed to trigger rescan for {folder_id}: {e}")
            return False

    def get_folder_status(self, folder_id: str) -> Optional[Dict]:
        """Get status of a specific folder"""
        try:
            url = f"{self.gui_url}/rest/db/status?folder={folder_id}"
            result = subprocess.run(
                ['curl', '-s', '-H', f'X-API-Key: {self.api_key}', url],
                capture_output=True,
                text=True,
                timeout=10
            )

            if result.returncode == 0 and result.stdout:
                return json.loads(result.stdout)
        except Exception as e:
            print_error(f"Failed to get status for {folder_id}: {e}")

        return None

    def trigger_rescan_all(self) -> int:
        """Trigger rescan for all folders"""
        print_header("Triggering Syncthing rescan...")

        success_count = 0
        for folder_id in self.config.folders.keys():
            if self.trigger_rescan(folder_id):
                print_success(f"Rescan triggered for folder: {folder_id}")
                success_count += 1
            else:
                print_warning(f"Failed to trigger rescan for: {folder_id}")

        return success_count

    def verify_cleanup(self) -> None:
        """Verify cleanup by checking folder status"""
        print_header("Verifying cleanup...")

        for folder_id, folder_path in self.config.folders.items():
            status = self.get_folder_status(folder_id)
            if status:
                errors = status.get('errors', 0)
                invalid = status.get('invalid', '')

                if errors == 0 and not invalid:
                    print_success(f"{folder_id} ({folder_path}): Clean")
                else:
                    print_warning(f"{folder_id}: {errors} errors, invalid: {invalid}")


def confirm_action(summary: Dict[str, int]) -> bool:
    """Ask user to confirm cleanup"""
    if summary['total'] == 0:
        print_info("No items to clean up.")
        return False

    print(f"\n{Colors.YELLOW}About to delete {summary['total']} items.{Colors.RESET}")
    print("Type 'yes' to continue, anything else to cancel: ", end='')

    response = input().strip().lower()
    return response == 'yes'


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Clean up unexpected items in Syncthing sync folders',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (asks before deleting)
  %(prog)s

  # Dry run (show what would be deleted)
  %(prog)s --dry-run

  # Silent mode (delete without asking)
  %(prog)s --yes

  # Clean specific folders only
  %(prog)s --folders ~/Develop ~/Codes

  # Clean only conflict files and empty dirs
  %(prog)s --types conflicts empty

  # Verbose output
  %(prog)s --verbose
        """
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be deleted without actually deleting'
    )

    parser.add_argument(
        '--yes',
        action='store_true',
        help='Skip confirmation prompt'
    )

    parser.add_argument(
        '--folders',
        nargs='+',
        help='Specific folders to clean (default: all sync folders)'
    )

    parser.add_argument(
        '--types',
        nargs='+',
        choices=['conflicts', 'empty', 'temp', 'symlinks'],
        help='Types of items to clean (default: all)'
    )

    parser.add_argument(
        '--config',
        help='Path to Syncthing config.xml (auto-detected if not specified)'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed progress'
    )

    parser.add_argument(
        '--no-rescan',
        action='store_true',
        help='Skip triggering Syncthing rescan after cleanup'
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_arguments()

    try:
        # Load configuration
        config = SyncthingConfig(args.config)

        # Determine which folders to scan
        if args.folders:
            folders = args.folders
        else:
            folders = config.get_folder_paths()

        if not folders:
            print_error("No sync folders found in configuration")
            return 1

        # Scan for items
        scanner = CleanupScanner(folders, verbose=args.verbose)
        scanner.scan(types=set(args.types) if args.types else None)

        # Show results
        scanner.print_results()

        # Check if dry run
        if args.dry_run:
            print_info("Dry run mode - no files were deleted")
            return 0

        # Confirm cleanup
        if not args.yes:
            if not confirm_action(scanner.get_summary()):
                print_info("Cleanup cancelled")
                return 0

        # Execute cleanup
        executor = CleanupExecutor(scanner, verbose=args.verbose)
        executor.execute()

        # Trigger rescan
        if not args.no_rescan and config.api_key:
            api = SyncthingAPI(config)
            api.trigger_rescan_all()

            # Wait a moment for scan to start
            import time
            time.sleep(3)

            # Verify cleanup
            api.verify_cleanup()

        print_success("\nCleanup completed!")
        return 0

    except FileNotFoundError as e:
        print_error(str(e))
        return 1
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
