# Network Connectivity Checker

A Python command-line tool that checks TCP connectivity to a specified hostname or IP address and port.

## Features

- Tests TCP connectivity using sockets.
- Supports hostnames and IP addresses.
- Uses a configurable connection timeout.
- Handles connection timeouts, refused connections, DNS failures, and other network errors.
- Validates port numbers.
- Includes automated tests using pytest.

## Requirements

- Python 3.14 or compatible Python 3 version.
- pytest for running tests.

## Usage

Check HTTPS connectivity:

```powershell
python network_checker.py --host google.com --port 443
```

Example successful output:

```text
[OK] google.com:443 - TCP connection successful
```

Check another port:

```powershell
python network_checker.py --host google.com --port 22
```

The result depends on whether the destination accepts TCP connections on that port.

## Run Tests

```powershell
python -m pytest -v
```

## Technical Details

The tool uses Python's `socket` module to establish TCP connections and `argparse` to process command-line arguments. Automated tests mock network operations to test different outcomes without relying on real network connections.

**Note:** This tool verifies TCP connectivity only. It does not verify TLS certificates, HTTP responses, or application-level health.
