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
    except socket.error:    #aborts program if there is an error
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
                    data = conn.recv(16) #b''
                    #if not data:
                     #   print("No data was received")
                      #  break
                    print('received "{0}"'.format(data.decode('utf8')))
                    conn.sendall(data, file=log_buffer)    # I am guessing on that log buffer...
                    print('sent "{0}"'.format(data.decode('utf8')))
                    
                    # TODO: Check here to see whether you have received the end
                    # of the message. If you have, then break from the `while True`
                    # loop.
                    # 
                    # Figuring out whether or not you have received the end of the
                    # message is a trick we learned in the lesson: if you don't
                    # remember then ask your classmates or instructor for a clue.
                    # :)

            finally:
                sock.close()
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
