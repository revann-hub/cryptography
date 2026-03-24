import random

def key_stream(seed, length):
    random.seed(seed)
    stream = bytearray()
    for _ in range(length):
        stream.append(random.randint(0, 255))
    return bytes(stream)

def to_bits(data):
    return " ".join(format(b, "08b") for b in data)

def xor_encrypt(text, key):
    text_bytes = text.encode()
    return bytes([tb ^ key[i] for i, tb in enumerate(text_bytes)])

def xor_decrypt(cipher, key):
    return "".join(chr(cb ^ key[i]) for i, cb in enumerate(cipher))


plaintext = input("Enter message: ")
seed_val = int(input("Enter seed: "))

plain_bytes = plaintext.encode()
key = key_stream(seed_val, len(plain_bytes))
cipher = xor_encrypt(plaintext, key)
decoded = xor_decrypt(cipher, key)

print("Plaintext bits:", to_bits(plain_bytes))
print("Cipher bits:", to_bits(cipher))
print("Decrypted text:", decoded)