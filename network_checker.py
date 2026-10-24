import socket
import argparse


def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True, "TCP connection successful"
    except socket.timeout:
        return False, "Connection timed out"
    except ConnectionRefusedError:
        return False, "Connection refused"
    except socket.gaierror:
        return False, "DNS resolution failed"
    except OSError as error:
        return False, f"Network error: {error}"



def main():
    parser = argparse.ArgumentParser(
        description="Check TCP connectivity to a host and port"
    )

    parser.add_argument("--host", required=True, help="Hostname or IP address")
    parser.add_argument("--port", type=int, required=True, help="TCP port number")

    args = parser.parse_args()
    
    if not 1 <= args.port <= 65535:
        parser.error("Port must be between 1 and 65535.")

    reachable, message = check_port(args.host, args.port)

    status = "OK" if reachable else "FAILED"
    print(f"[{status}] {args.host}:{args.port} - {message}")


if __name__ == "__main__":
    main()
