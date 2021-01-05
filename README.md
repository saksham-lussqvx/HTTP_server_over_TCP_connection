# HTTP_server_over_TCP_connection
This is a simple server creation script with client also. It can host a TCP server with integrated HTTP server and the client can download file with status based response.

### TCP_server
This script creates a TCP server which has a HTTP_request handler. The server cn host files of the current directory and client can download files from it.
Usage - python3 TCPserver.py -a localhost -p 8000 or python3 TCPserver.py --addr localhost --port 8000
### TCP client
This script can download the selected sile from the hosted server. It stores the file in the directory from where this script is running. This script runs only on windows, but if you want you can modify it to run it in linux also.
Usage - python3 TCPserver.py --addr localhost --port 8000 --file yourfile.txt or python3 TCPserver.py -ad localhost -p 8000 -f yourfile.txt
