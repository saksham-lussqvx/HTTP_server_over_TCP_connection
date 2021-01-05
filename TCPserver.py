from http.server import SimpleHTTPRequestHandler
import socketserver
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-a",
        "--addr",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )

    args = parser.parse_args()
    with socketserver.TCPServer((args.addr, args.port), SimpleHTTPRequestHandler) as httpd:
        print("The server is ready to receive...")
        httpd.serve_forever()
        
