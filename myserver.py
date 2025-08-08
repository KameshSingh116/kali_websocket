import socket
import sys

HOST=''
PORT=8080


mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("The socket  has been created!!")

try:
   mysocket.bind((HOST,PORT))
except socket.error as msg:
   print(f"Binding has failed. Error Code is: {str(msg[0])} message: {msg[1]}")
   sys.exit()

print("Socket binding is complete !, now we can proceed with the socket listening!")\

mysocket.listen(10)
print("Socket is now listening!!")

while 1:
      connection,address=mysocket.accept()
      print(f"Connection with {address[0]} : {str(address[1])}")

mysocket.close()

