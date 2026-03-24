def gcd_simple(a, b):
    while b:
        a, b = b, a % b
    return a


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    q, r = divmod(a, b)
    g, x1, y1 = egcd(b, r)
    return g, y1, x1 - q * y1


def mod_inv(e, phi):
    g, x, _ = egcd(e, phi)
    if g != 1:
        return None
    return x % phi


def rsa_enc(msg, e, n):
    return pow(msg, e, n)


def rsa_dec(cipher, d, n):
    return pow(cipher, d, n)


p = int(input("Prime p: "))
q = int(input("Prime q: "))
e = int(input("Public exponent e: "))
msg = int(input("Message m: "))

n = p * q
phi = (p - 1) * (q - 1)

if gcd_simple(e, phi) != 1:
    print("Error: e and φ(N) must be coprime")
elif not (0 < msg < n):
    print("Error: message must satisfy 0 < m < N")
elif gcd_simple(msg, n) != 1:
    print("Error: message must be in Z*_N")
else:
    d = mod_inv(e, phi)
    cipher = rsa_enc(msg, e, n)
    plain = rsa_dec(cipher, d, n)

    print("Ciphertext:", cipher)
    print("Decrypted:", plain)
