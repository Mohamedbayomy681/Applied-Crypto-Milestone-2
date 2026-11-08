
import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

KEY = b"BankKey1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server is waiting for a connection...")

connection, address = server.accept()
print("Client connected:", address)

encrypted_data = connection.recv(4096)

cipher = DES.new(KEY, DES.MODE_ECB)
decrypted_data = unpad(cipher.decrypt(encrypted_data), DES.block_size)

print("Received transaction:", decrypted_data.decode("utf-8"))

connection.close()
server.close()
