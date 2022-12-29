#import sys
#print("User current Version:-",sys.version)

import socket
hostname=socket.gethostname()
print(hostname)

ipadd = socket.gethostbyname(hostname)
print(ipadd)