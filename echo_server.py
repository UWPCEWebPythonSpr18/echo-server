import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    try:
        sock.bind(address)
    except socket.error:    # aborts program if there is an error
        print("Unable to create socket.")
        sock.close()
        exit()

    sock.listen(1)
    print("Socket is listening for connections.")
    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('Waiting for a connection...', file=log_buffer)
            conn, addr = sock.accept()
            try:
                print('Connection - {0}:{1}'.format(*addr), file=log_buffer)
                while True:
                    data = conn.recv(16)
                    print('received "{0}"'.format(data.decode('utf8')))
                    conn.sendall(data)
                    print('sent "{0}"'.format(data.decode('utf8')))
                    if len(data) < 16:
                        print("Reached EOM")
                        break
                        sock.close()
            finally:
                print(
                    'Echo complete, client connection closed', file=log_buffer
                )
    except KeyboardInterrupt:
        sock.close()
        print()
        print('User Inturrupt:  Closing Socket.', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
