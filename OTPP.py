import os

def make_key(size):
    return os.urandom(size)

def bits_view(data):
    return " ".join(format(b, "08b") for b in data)

def xor_enc(text, key):
    text_bytes = text.encode()
    return bytes([tb ^ key[i] for i, tb in enumerate(text_bytes)])

def xor_dec(cipher, key):
    return "".join(chr(cb ^ key[i]) for i, cb in enumerate(cipher))


message = input("Enter message: ")

plain_bytes = message.encode()
key = make_key(len(plain_bytes))
cipher = xor_enc(message, key)
decoded = xor_dec(cipher, key)

print("Plaintext bits:", bits_view(plain_bytes))
print("Cipher bits:", bits_view(cipher))
print("Decrypted text:", decoded)
