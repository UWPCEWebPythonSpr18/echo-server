"""
Function to list services of all dedicated ports.
"""

import random
import socket

def porter(port=0):     
    service = {}
    try:
        info = socket.getservbyport(port)
        service[port] = info
        return info

    except OSError as e:
        return None


if __name__ == "__main__":
    # porter(random.randint(0, 65535))
    book = {}
    for x in range(0, 65535+1):
        received = porter(x)
        if received:
            book[x] = received
    
    for key, val in book.items():
        print(f"Port: {key} | Service: {val}")
