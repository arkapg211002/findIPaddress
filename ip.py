'''import  socket
hostname=socket.gethostname()
address=socket.gethostbyname(hostname)
print("computer name is ",hostname)
print("computer ip address ",address)'''
import socket
host=socket.gethostname()
add=socket.gethostbyname(host)
print("computer name ",host)
print(" ip address ",add)