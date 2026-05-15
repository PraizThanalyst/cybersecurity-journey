import base64

text = "SilentPayload"
encoded = base64.b64encode(text.encode())
print(encoded.decode())

decoded = base64.b64decode(encoded)
print(decoded.decode())

print()

cookie = "eyJ1c2VyIjoiYWRtaW4ifQ=="

decoded = base64.b64decode(cookie).decode()
print(decoded)

print()


text = "SilentPayload"
hex_encoded = text.encode().hex()
print(hex_encoded)



hex_decoded = bytes.fromhex(hex_encoded).decode()
print(hex_decoded)


print()

import hashlib

text = "SilentPayload"


md5 = hashlib.md5(text.encode()).hexdigest()

sha256 = hashlib.sha256(text.encode()).hexdigest()

print("MD5: ", md5)
print("SHA256: ", sha256)

print()

text2 = "silentPayload"

md52 = hashlib.md5(text2.encode()).hexdigest()

sha2562 = hashlib.sha256(text2.encode()).hexdigest()

print("MD5: ", md52)
print("SHA256: ", sha2562)

print()

import os

password = "password123"
salt = os.urandom(16).hex()
salted = password + salt
salted_hash = hashlib.sha256(salted.encode()).hexdigest()

print("Salt:", salt)
print("Salted Hash: ", salted_hash)


