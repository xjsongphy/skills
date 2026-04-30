# Implementation Details

## Script Architecture

The cleanup script is organized into several classes for maintainability:

### SyncthingConfig
- Parses `config.xml` to extract sync folders, API key, and GUI URL
- Supports automatic config detection across platforms
- Expands `~` in folder paths

### CleanupScanner
- Scans folders for different types of unexpected items
- Supports filtering by type (conflicts, empty, temp, symlinks)
- Provides detailed summary of findings

### CleanupExecutor
- Performs actual deletion operations
- Handles errors gracefully
- Reports detailed statistics

### SyncthingAPI
- Interacts with Syncthing REST API
- Triggers folder rescans
- Verifies cleanup results

## Error Handling

The script handles various error conditions:

- **Missing config**: Provides helpful error message with config locations
- **Permission errors**: Logs errors but continues with other files
- **API failures**: Falls back gracefully; cleanup still succeeds
- **Network issues**: Timeout handling for curl commands

## Performance Considerations

- **Recursive scanning**: Uses `Path.rglob()` for efficient traversal
- **Sorted deletion**: Empty directories deleted deepest-first
- **Parallel operations**: Could be enhanced for concurrent folder scanning
- **Memory efficient**: Uses generators where possible

## Security Features

- **Confirmation prompt**: Requires user confirmation before deletion
- **Dry-run mode**: Preview deletions without executing
- **Folder validation**: Only operates on known Syncthing folders
- **API key protection**: Extracts from config; never exposes in logs

## Extensibility

To add new cleanup types:

1. Add scan method to `CleanupScanner`:
```python
def _scan_new_type(self, folder: str) -> None:
    # Find items of new type
    items = list(Path(folder).rglob("pattern"))
    self.new_type.extend(items)
```

2. Add counter to `CleanupExecutor`:
```python
self.deleted_new_type = 0
```

3. Add deletion method:
```python
def _delete_new_type(self) -> None:
    for item in self.scanner.new_type:
        # Delete with error handling
```

4. Update summary and reporting accordingly

## API Integration

The script uses Syncthing's REST API:

### Endpoints Used
- `POST /rest/db/scan?folder=<id>` - Trigger folder scan
- `GET /rest/db/status?folder=<id>` - Get folder status

### Authentication
Uses `X-API-Key` header with key from `config.xml`

### Error Handling
- Checks HTTP response codes
- Validates JSON responses
- Provides user-friendly error messages

## Cross-Platform Support

The script works across platforms:

### Linux
- Config: `~/.config/syncthing/config.xml`
- Paths: POSIX paths with `/`

### macOS
- Config: `~/Library/Application Support/Syncthing/config.xml`
- Paths: POSIX paths with `/`

### Windows (via WSL)
- Config: `~/.config/syncthing/config.xml`
- Paths: POSIX paths via WSL

## Dependencies

The script uses only Python standard library:
- `pathlib` - Path operations
- `re` - Config parsing
- `subprocess` - API calls via curl
- `argparse` - CLI arguments
- `json` - API response parsing

No external dependencies required!
