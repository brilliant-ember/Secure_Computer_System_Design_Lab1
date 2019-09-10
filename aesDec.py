from Crypto.Cipher import AES

file_to_dycrypt = open("./encrypted.bin", "rb")
nonce, tag, ciphertext = [file_to_dycrypt.read(x) for x in (16, 16, -1)]

key = open("./key", "rb").read()

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)