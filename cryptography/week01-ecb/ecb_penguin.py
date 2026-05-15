from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

KEY = b"YELLOW SUBMARINE"  # exactly 16 bytes = 128-bit AES key
BLOCK_SIZE = 16

with open("tux.bmp", "rb") as f:
    data = f.read()

header = data[:138]
body = data[138:]

padded_body = pad(body, BLOCK_SIZE)

cipher = AES.new(KEY, AES.MODE_ECB)
encrypted_body = cipher.encrypt(padded_body)

# Truncate encrypted body to original body length so file size matches
encrypted_body = encrypted_body[:len(body)]

with open("tux_ecb.bmp", "wb") as f:
    f.write(header + encrypted_body)

print(f"Original size: {len(data)} bytes")
print(f"Encrypted file written: tux_ecb.bmp")
