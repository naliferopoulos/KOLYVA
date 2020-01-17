import socket
import sys

target = str(sys.argv[1])

with open("dyn.lst", "r") as f:
    for word in f.readlines():
        #print("Attempting " + target + "." + word[:-1])
        try:
            print(socket.gethostbyname(target + "." + word[:-1]), end=' ')
            print("-", end = ' ')
            print(target + "." + word[:-1])
        except:
            pass
            