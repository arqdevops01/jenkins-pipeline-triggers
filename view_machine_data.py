import socket
import os

def main():
    hostname = socket.gethostname()
    print(f"Name of the server: {hostname}")
    # print(f'The current directory is: {os.getcwd()}')

if __name__ == "__main__":
    main()
        