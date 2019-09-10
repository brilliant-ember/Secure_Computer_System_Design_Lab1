from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key_path = "./key"
key_file = open(key_path, "wb")
key = get_random_bytes(16) #16 bytes *8 = number of bits (byte =8)
key_file.write(key)
print("Generated and wrote the key to the key file")
key_file.close()

cipher = AES.new(key, AES.MODE_EAX)
secret = "Mo is Mo"
secret_bytes = str.encode(secret)
# print(secret_bytes)
ciphertext, tag = cipher.encrypt_and_digest(secret_bytes)

file_out = open("./encrypted.bin", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]