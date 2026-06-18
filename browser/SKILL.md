---
name: browser
description: Use when building browser automation scripts that need to control Chrome via the AgentInBrowser REST API. Covers how to start/stop the server, send commands, and handle responses.
---

# AgentInBrowser Skill

## Overview

AgentInBrowser is a REST API service that provides remote control of a Chrome browser. It wraps Selenium WebDriver and exposes HTTP endpoints for browser operations (find elements, click, type, screenshot, execute JS, etc.).

**Project Location**: `D:\Develop\AgentInBrowser`

## When to Use

- Building browser automation scripts (auto-login, course watching, form filling, etc.)
- Need to control browser via HTTP interface instead of using Selenium directly
- Need to run browser tasks in background without detection

## Quick Reference

### Start Server

```bash
# In project directory (using uv)
cd D:\Develop\AgentInBrowser
source .venv/bin/activate  # Linux/macOS
# or .venv\Scripts\activate  # Windows
aib

# Or use directly after global install
aib
```

Server listens on: `http://127.0.0.1:5000`

### Check Server Status

```python
import requests
resp = requests.get("http://127.0.0.1:5000/status")
# → {"status": "running", "browser_active": false, "current_url": null}
```

### Stop Server

```python
requests.post("http://127.0.0.1:5000/shutdown")  # Close browser + exit server
requests.post("http://127.0.0.1:5000/quit")      # Close browser only, server stays alive
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/status` | GET | Get server status |
| `/env` | GET | Get server environment info (project dir, venv path, etc.) |
| `/init` | POST | Initialize browser and navigate to URL |
| `/execute` | POST | Execute a Selenium command |
| `/quit` | POST | Close browser (server continues) |
| `/shutdown` | POST | Close browser and stop server |

---

## Agent Usage Workflow (Important!)

Since the server uses `uv` for dependency management, the virtual environment `.venv` is inside the project directory. Agent's bash tool runs in a local directory, so you need to get server environment info first before activating venv.

### Step 1: Query Server Environment

```python
import requests

env = requests.get("http://127.0.0.1:5000/env").json()
print(env)
# → {
#     "project_dir": "D:\\Develop\\AgentInBrowser",
#     "venv_path": "D:\\Develop\\AgentInBrowser\\.venv",
#     "python_executable": "D:\\Develop\\AgentInBrowser\\.venv\\Scripts\\python.exe",
#     "platform": "Windows",
#     "is_windows": true,
#     "activate_cmd": "D:\\Develop\\AgentInBrowser\\.venv\\Scripts\\activate.bat",
#     "activate_ps": "D:\\Develop\\AgentInBrowser\\.venv\\Scripts\\Activate.ps1"
#   }
```

### Step 2: Activate venv (Execute Before Using CLI)

In Agent's bash command, activate venv first before using `aib-client`:

**Windows PowerShell:**
```bash
& "D:\Develop\AgentInBrowser\.venv\Scripts\Activate.ps1"
aib-client init https://example.com
```

**Windows cmd:**
```bash
D:\Develop\AgentInBrowser\.venv\Scripts\activate.bat && aib-client init https://example.com
```

**Linux/macOS:**
```bash
source /path/to/AgentInBrowser/.venv/bin/activate
aib-client init https://example.com
```

### Step 3: Use CLI Client

```bash
# Now aib-client is available
aib-client init https://example.com
aib-client find button
aib-client click 0
aib-client quit
```

---

## Response Format

All endpoints return JSON with unified format:

```json
// Success
{"success": true, "data": {...}}

// Failure
{"success": false, "error": "error message"}
```

## Commands via `/execute`

Request body format:

```json
{"cmd": "command_name", "params": {"key": "value"}}
```

### Finding Elements

#### `find` — Find elements by CSS selector

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "find",
    "params": {"selector": "button.btn-primary"}
})
# → {"success": true, "data": {
#     "count": 3,
#     "elements": [
#       {"index": 0, "tag": "button", "text": "Login", "class": "btn-primary", "id": ""},
#       ...
#     ]
#   }}
```

**Note**: `find` results are cached, subsequent `click`/`send_keys`/`get_html` reference by index.

#### `inputs` — Get all input elements

```python
requests.post("http://127.0.0.1:5000/execute", json={"cmd": "inputs"})
# → {"success": true, "data": {
#     "count": 2,
#     "inputs": [
#       {"index": 0, "type": "text", "name": "username", "placeholder": "Username", ...},
#       ...
#     ]
#   }}
```

#### `buttons` — Get all button elements

```python
requests.post("http://127.0.0.1:5000/execute", json={"cmd": "buttons"})
# → {"success": true, "data": {
#     "count": 1,
#     "buttons": [
#       {"index": 0, "text": "Submit", "class": "submit-btn", "id": ""}
#     ]
#   }}
```

### Element Interaction

#### `click` — Click element (by index from find/inputs/buttons)

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "click",
    "params": {"index": 0}
})
# → {"success": true, "data": {"current_url": "https://..."}}
```

Auto-scrolls to element visible area, falls back to JS click on normal click failure. Built-in random delays mimic human behavior.

#### `send_keys` — Type text into element

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "send_keys",
    "params": {"index": 0, "text": "hello"}
})
# → {"success": true, "data": {"success": true}}
```

Calls `clear()` first before typing, built-in random delays.

### Page Information

#### `page_info` — Get current page information

```python
requests.post("http://127.0.0.1:5000/execute", json={"cmd": "page_info"})
# → {"success": true, "data": {"url": "...", "title": "...", "source_length": 12345}}
```

#### `get_text` — Get page text

```python
requests.post("http://127.0.0.1:5000/execute", json={"cmd": "get_text"})
# → {"success": true, "data": {"text": "page body text (first 2000 chars)"}}
```

#### `get_html` — Get element innerHTML

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "get_html",
    "params": {"index": 0}
})
# → {"success": true, "data": {"html": "...(max 5000 chars)"}}
```

### Utility Commands

#### `screenshot` — Take screenshot

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "screenshot",
    "params": {"filename": "my_screenshot.png"}  # optional, defaults to timestamp filename
})
# → {"success": true, "data": {"filename": "my_screenshot.png"}}
```

#### `execute_script` — Execute JavaScript

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "execute_script",
    "params": {"script": "return document.title"}
})
# → {"success": true, "data": {"result": "page title"}}
```

#### `sleep` — Wait (also saves page HTML)

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "sleep",
    "params": {"seconds": 5}
})
# → {"success": true, "data": {"slept": 5}}
```

### Window Management

#### `switch_window` — Switch window

```python
requests.post("http://127.0.0.1:5000/execute", json={
    "cmd": "switch_window",
    "params": {"index": -1}  # -1 = newest window, 0/1/2 = specific index
})
# → {"success": true, "data": {"current_url": "...", "title": "...", "window_count": 2}}
```

#### `close_window` — Close current window (auto-switch back to main window)

```python
requests.post("http://127.0.0.1:5000/execute", json={"cmd": "close_window"})
# → {"success": true, "data": {"current_url": "...", "title": "..."}}
```

## Typical Workflow

### 1. Initialize browser and open page

```python
import requests

SERVER = "http://127.0.0.1:5000"

# Initialize browser and navigate to URL
resp = requests.post(f"{SERVER}/init", json={"url": "https://example.com"})
print(resp.json())
```

### 2. Find and interact

```python
# Find all links
resp = requests.post(f"{SERVER}/execute", json={
    "cmd": "find", "params": {"selector": "a"}
})
elements = resp.json()["data"]["elements"]

# Click first one
requests.post(f"{SERVER}/execute", json={
    "cmd": "click", "params": {"index": 0}
})

# Wait for page load
requests.post(f"{SERVER}/execute", json={
    "cmd": "sleep", "params": {"seconds": 3}
})
```

### 3. Fill form

```python
# Get input fields
requests.post(f"{SERVER}/execute", json={"cmd": "inputs"})

# Fill them
requests.post(f"{SERVER}/execute", json={
    "cmd": "send_keys", "params": {"index": 0, "text": "username"}
})
requests.post(f"{SERVER}/execute", json={
    "cmd": "send_keys", "params": {"index": 1, "text": "password"}
})

# Get buttons and click
requests.post(f"{SERVER}/execute", json={"cmd": "buttons"})
requests.post(f"{SERVER}/execute", json={
    "cmd": "click", "params": {"index": 0}
})
```

### 4. Handle new window (e.g., popup login)

```python
# Switch to newest window
requests.post(f"{SERVER}/execute", json={
    "cmd": "switch_window", "params": {"index": -1}
})

# ... interact in new window ...

# Close new window, return to main window
requests.post(f"{SERVER}/execute", json={"cmd": "close_window"})
```

### 5. Cleanup

```python
# Close browser, server continues running
requests.post(f"{SERVER}/quit")

# Or completely shutdown
requests.post(f"{SERVER}/shutdown")
```

## Important Notes

1. **Element indices are ephemeral** — Each `find`/`inputs`/`buttons` call resets internal cache, subsequent `click`/`send_keys`/`get_html` reference the most recent find result
2. **Server must be started first** — Client scripts should check `/status` before sending commands
3. **Anti-detection is built-in** — Server automatically injects anti-suspend scripts and anti-automation detection, no client-side work needed
4. **Random delays included** — `click` and `send_keys` include random delays to mimic human behavior
5. **Auto-logging** — All operations logged to `server_log.txt` in working directory
6. **Click auto-fallback** — Falls back to JavaScript click when normal click fails
