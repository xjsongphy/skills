#!/usr/bin/env python3
"""
Test script for syncthing-cleanup skill

Creates test files and directories to demonstrate the cleanup functionality.
Run in a test directory to see how the cleanup script works.
"""

import os
import shutil
from pathlib import Path


def create_test_environment(test_dir: str = "./syncthing-test") -> None:
    """Create test environment with various unexpected items"""

    test_path = Path(test_dir).absolute()

    # Clean up existing test directory
    if test_path.exists():
        shutil.rmtree(test_path)

    test_path.mkdir()

    print(f"Creating test environment in: {test_path}")

    # Create directory structure
    (test_path / "0.syncthing-enc" / "subdir").mkdir(parents=True)
    (test_path / "A.syncthing-enc" / "deep" / "nested").mkdir(parents=True)

    # Create conflict files
    (test_path / "0.syncthing-enc" / "file.txt.sync-conflict-20240101").write_text("conflict content")
    (test_path / "A.syncthing-enc" / "deep" / "doc.txt.sync-conflict-20240102").write_text("another conflict")

    # Create empty directories
    (test_path / "0.syncthing-enc" / "empty1").mkdir()
    (test_path / "A.syncthing-enc" / "deep" / "empty2").mkdir()

    # Create temporary files
    (test_path / "0.syncthing-enc" / ".DS_Store").write_text("macos metadata")
    (test_path / "A.syncthing-enc" / "swpfile.swp").write_text("vim swap")
    (test_path / "0.syncthing-enc" / "backup~").write_text("backup file")
    (test_path / "A.syncthing-enc" / "temp.tmp").write_text("temp file")

    # Create normal files (should not be deleted)
    (test_path / "0.syncthing-enc" / "normal.txt").write_text("normal file")
    (test_path / "A.syncthing-enc" / "document.pdf").write_text("pdf content")

    # Create broken symlink
    (test_path / "0.syncthing-enc" / "broken_link").symlink_to("/nonexistent/path")

    print("\n✓ Test environment created!")
    print(f"\nTest directory: {test_path}")
    print("\nContents:")
    for item in test_path.rglob("*"):
        if item.is_file():
            print(f"  📄 {item.relative_to(test_path)}")
        elif item.is_dir():
            print(f"  📁 {item.relative_to(test_path)}/")

    print(f"\nTo test cleanup, run:")
    print(f"  python3 scripts/cleanup_syncthing.py --folders {test_dir} --dry-run")
    print(f"  python3 scripts/cleanup_syncthing.py --folders {test_dir} --yes")


def cleanup_test_environment(test_dir: str = "./syncthing-test") -> None:
    """Remove test environment"""

    test_path = Path(test_dir).absolute()

    if test_path.exists():
        shutil.rmtree(test_path)
        print(f"✓ Test environment removed: {test_path}")
    else:
        print(f"Test environment not found: {test_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        cleanup_test_environment()
    else:
        create_test_environment()
