import socket
s = socket.socket()
print("socket successfully created")
port = 40674
s.bind(('', port))
print("socket bind to %s" %(port))
s.listen(5)
print("socket is listening")
while True:
    c,addr = s.accept() #
    print('Got connect from',addr) # single line,multiple variables
    c.send(b'Thanking for connecting')
    c.close()
