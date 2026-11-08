
import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# Same 64-bit key used by the server
KEY = b"BankKey1"

# Banking transaction
message = input("Enter your banking transaction: ")

# Encrypt using DES in ECB mode
cipher = DES.new(KEY, DES.MODE_ECB)
encrypted_data = cipher.encrypt(pad(message.encode("utf-8"), DES.block_size))

print("Original transaction:", message)
print("Encrypted transaction:", encrypted_data.hex())

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

# Send encrypted transaction
client.sendall(encrypted_data)

print("Encrypted transaction sent successfully!")

client.close()
