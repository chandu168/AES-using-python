# generate new instance with the key and nonce same as encryption cipher
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# decrypt the data
plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext)
