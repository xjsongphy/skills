---
name: syncthing-cleanup
description: Use when cleaning up Syncthing sync folders with conflict files (.sync-conflict-*), empty directories, temporary files, or other unexpected artifacts.
---

# Syncthing Cleanup

## Overview

Syncthing creates various temporary and conflict files during synchronization, which accumulate over time and may appear as "unexpected items" in the Web UI. This skill identifies and safely removes these artifacts.

## Quick Start

To clean up Syncthing folders:

```bash
# Run the cleanup script
scripts/cleanup_syncthing.py
```

The script will:
1. Locate Syncthing configuration and sync folders
2. Scan for unexpected items
3. Show what will be deleted
4. Ask for confirmation before deleting
5. Trigger rescan and report results

## What Gets Cleaned

### Conflict Files
- `.sync-conflict-*` - Created when multiple devices modify the same file simultaneously

### Empty Directories
- Empty directories within `.syncthing-enc` folders (encrypted storage)

### Temporary Files
- `*.swp`, `*.swo` - Vim swap files
- `*~` - Backup files
- `.DS_Store` - macOS metadata files
- `Thumbs.db` - Windows thumbnail cache
- `*.tmp` - Generic temporary files

### Broken Symlinks
- Symbolic links pointing to non-existent targets

## Using the Cleanup Script

### Basic Usage

```bash
# Interactive mode (asks before deleting)
scripts/cleanup_syncthing.py

# Dry run (show what would be deleted)
scripts/cleanup_syncthing.py --dry-run

# Silent mode (delete without asking)
scripts/cleanup_syncthing.py --yes

# Clean specific folders only
scripts/cleanup_syncthing.py --folders ~/Develop ~/Codes

# Verbose output
scripts/cleanup_syncthing.py --verbose
```

### Script Options

| Option | Description |
|--------|-------------|
| `--dry-run` | Show what would be deleted without actually deleting |
| `--yes` | Skip confirmation prompt |
| `--folders PATH [PATH ...]` | Only clean specified folders |
| `--types TYPE [TYPE ...]` | Only clean specific types (conflicts, empty, temp, symlinks) |
| `--verbose` | Show detailed progress |
| `--api-key KEY` | Syncthing API key (auto-detected from config) |
| `--gui-url URL` | Syncthing GUI URL (auto-detected from config) |

## Manual Cleanup Steps

If you need to manually clean up or understand what the script does:

### 1. Find Conflict Files

```bash
find ~/Develop ~/大学 ~/skills ~/Codes -name "*.sync-conflict-*"
```

### 2. Find Empty Directories

```bash
find ~/Develop ~/大学 ~/skills ~/Codes -type d -empty
```

### 3. Find Temporary Files

```bash
find ~/Develop ~/大学 ~/skills ~/Codes \( -name "*.swp" -o -name "*~" -o -name ".DS_Store" -o -name "Thumbs.db" -o -name "*.tmp" \)
```

### 4. Delete Items

After verifying the items are safe to delete:

```bash
# Delete conflict files
find ~/Develop ~/大学 ~/skills ~/Codes -name "*.sync-conflict-*" -delete

# Delete empty directories
find ~/Develop ~/大学 ~/skills ~/Codes -type d -empty -delete

# Delete temporary files
find ~/Develop ~/大学 ~/skills ~/Codes \( -name "*.swp" -o -name "*~" -o -name ".DS_Store" -o -name "Thumbs.db" -o -name "*.tmp" \) -delete
```

### 5. Trigger Rescan

Use the Syncthing API to rescan all folders:

```bash
# Get API key and GUI URL from config
API_KEY=$(grep -oP '(?<=<apikey>)[^<]+' ~/.config/syncthing/config.xml)
GUI_URL=$(grep -oP '(?<=<address>)[^<]+' ~/.config/syncthing/config.xml)

# Rescan all folders
for folder in $(grep -oP '(?<=<folder id=")[^"]+' ~/.config/syncthing/config.xml); do
    curl -s -X POST -H "X-API-Key: $API_KEY" "http://$GUI_URL/rest/db/scan?folder=$folder"
done
```

### 6. Verify Status

```bash
# Check folder status via API
curl -s -H "X-API-Key: $API_KEY" "http://$GUI_URL/rest/db/status?folder=FOLDER_ID" | jq '.'
```

## After Cleanup

After cleaning up:

1. **Refresh the Web UI** - Open http://localhost:8384 (or your configured port) to verify unexpected items are gone

2. **Monitor for new conflicts** - If conflicts keep appearing, check:
   - Are multiple devices editing the same files simultaneously?
   - Do you have clock synchronization issues between devices?
   - Are there permission problems?

3. **Consider ignore patterns** - For files that repeatedly create conflicts, add them to `.stignore`:
   ```
   # Ignore temporary files
   *.tmp
   *.swp
   *~
   .DS_Store
   Thumbs.db
   ```

## Troubleshooting

### Unexpected Items Still Show After Cleanup

1. **Rescan didn't complete** - Wait a few seconds and refresh the Web UI
2. **Items are in subdirectories** - The script searches recursively, but if you used `--folders`, ensure all paths are included
3. **Cached data** - Try restarting Syncthing:
   ```bash
   pkill syncthing
   syncthing serve --no-browser --no-restart &
   ```

### Script Can't Find Configuration

The script looks for configuration in:
- `~/.config/syncthing/config.xml`
- `~/.syncthing/config.xml`
- `~/Library/Application Support/Syncthing/config.xml` (macOS)

If your config is elsewhere, specify it:
```bash
scripts/cleanup_syncthing.py --config /path/to/config.xml
```

### Permission Errors

Some files may require elevated permissions. The script will report what it couldn't delete. You can:

1. Run with sudo (use carefully):
   ```bash
   sudo scripts/cleanup_syncthing.py
   ```

2. Fix permissions manually:
   ```bash
   sudo chown -R $USER:$(id -gn) ~/Develop ~/大学 ~/skills ~/Codes
   ```

## Safety Features

The cleanup script includes several safety features:

- **Dry run mode** - Preview deletions without executing
- **Confirmation prompt** - Requires confirmation before deleting (unless `--yes` is used)
- **Detailed logging** - Shows exactly what was deleted
- **Folder validation** - Only operates on known Syncthing folders
- **API verification** - Uses official Syncthing API for operations

## Integration with Syncthing

This skill integrates with Syncthing's REST API:

- **Reading configuration** - Extracts folder paths and API credentials
- **Triggering scans** - Requests folder rescans after cleanup
- **Checking status** - Verifies cleanup results

API endpoints used:
- `GET /rest/system/status` - System information
- `GET /rest/db/status?folder=<id>` - Folder status
- `POST /rest/db/scan?folder=<id>` - Trigger folder scan

## Best Practices

1. **Run dry-run first** - Always preview with `--dry-run` before actual cleanup
2. **Backup important data** - Although cleanup is safe, backups are prudent
3. **Schedule regular cleanup** - Set up a cron job or systemd timer for automatic cleanup
4. **Monitor conflict patterns** - Frequent conflicts may indicate workflow issues
5. **Keep ignore patterns updated** - Add commonly conflicting file types to `.stignore`
