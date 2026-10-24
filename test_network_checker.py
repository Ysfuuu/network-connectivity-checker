from unittest.mock import patch
from network_checker import check_port
import socket
import subprocess
import sys


@patch("network_checker.socket.create_connection")
def test_check_port_success(mock_connection):
    mock_connection.return_value.__enter__.return_value = None

    reachable, message = check_port("google.com", 443)

    assert reachable is True
    assert message == "TCP connection successful"


@patch("network_checker.socket.create_connection")
def test_check_port_timeout(mock_connection):
    mock_connection.side_effect = socket.timeout

    reachable, message = check_port("google.com", 443)

    assert reachable is False
    assert message == "Connection timed out"

@patch("network_checker.socket.create_connection")
def test_check_port_dns_failure(mock_connection):
    mock_connection.side_effect = socket.gaierror

    reachable, message = check_port("invalid.example", 443)

    assert reachable is False
    assert message == "DNS resolution failed"

@patch("network_checker.socket.create_connection")
def test_check_port_connection_refused(mock_connection):
    mock_connection.side_effect = ConnectionRefusedError

    reachable, message = check_port("127.0.0.1", 8080)

    assert reachable is False
    assert message == "Connection refused"

@patch("network_checker.socket.create_connection")
def test_check_port_network_error(mock_connection):
    mock_connection.side_effect = OSError("Network is unreachable")

    reachable, message = check_port("example.com", 443)

    assert reachable is False
    assert message == "Network error: Network is unreachable"

def test_invalid_port():
    result = subprocess.run(
        [
            sys.executable,
            "network_checker.py",
            "--host", "google.com",
            "--port", "70000",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "Port must be between 1 and 65535." in result.stderr