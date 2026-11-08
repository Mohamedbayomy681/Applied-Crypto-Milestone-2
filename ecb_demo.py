
from Crypto.Cipher import DES

# Same 64-bit key
KEY = b"BankKey1"

# Two identical 8-byte blocks
block1 = b"BANKDATA"
block2 = b"BANKDATA"

# Encrypt using DES-ECB
cipher = DES.new(KEY, DES.MODE_ECB)

encrypted1 = cipher.encrypt(block1)
encrypted2 = cipher.encrypt(block2)

print("Plaintext Block 1:", block1)
print("Plaintext Block 2:", block2)

print("Ciphertext Block 1:", encrypted1.hex())
print("Ciphertext Block 2:", encrypted2.hex())

print("Are ciphertext blocks identical?", encrypted1 == encrypted2)
