import requests
import os
import argparse

class get_file:
    def __init__(self, filename, port, addr):
        self._filename = filename
        self._port = port
        self._addr = addr

    def file(self):
        print(f"""HTTP request to server: 
        GET: {self._filename}
        Host: {self._addr}""")
        url = "http://"+self._addr+":"+str(self._port)+"/"+self._filename
        r = requests.get(url)
        if r.status_code == 200:
            print(f"""HTTP response from server:  
            {r.status_code} OK""")
            loc = os.getcwd()
            location = loc+'/'+self._filename
            with open(location, 'wb') as f:
                f.write(r.content)
            print("done")
        elif r.status_code == 404:
            print(f"""HTTP response from server:  
            {r.status_code} File Not found""")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a HTTP server over TCP connection")
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
    parser.add_argument(
        "-f",
        "--file",
        default='',
        help="Specify the File to download (if located inside then enter the path also)",
    )
    args = parser.parse_args()
    fetch = get_file(args.file, args.port, args.addr)
    fetch.file()