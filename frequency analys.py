ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt_caesar(msg, step):
    out = []
    for symbol in msg:
        if symbol in ALPHABET:
            pos = ALPHABET.find(symbol)
            new_pos = (pos + step) % len(ALPHABET)
            out.append(ALPHABET[new_pos])
        else:
            out.append(symbol)
    return "".join(out)


def decrypt_caesar(msg, step):
    return encrypt_caesar(msg, -step)


def most_frequent_letter(txt):
    letters = [ch for ch in txt if ch in ALPHABET]
    if not letters:
        return None
    return max(letters, key=lambda c: letters.count(c))


ciphertext = input("Enter encrypted text: ").upper()
guess_shift = (ALPHABET.index(most_frequent_letter(ciphertext)) - ALPHABET.index("E")) % len(ALPHABET)
print("Plaintext:", decrypt_caesar(ciphertext, guess_shift))
