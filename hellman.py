def pub_key(base, priv, prime):
    return pow(base, priv, prime)


def shared_key(pub_other, priv, prime):
    return pow(pub_other, priv, prime)


prime = int(input("Enter prime q: "))
base = int(input("Enter generator g: "))

alice_priv = int(input("Alice private key: "))
bob_priv = int(input("Bob private key: "))

alice_pub = pub_key(base, alice_priv, prime)
bob_pub = pub_key(base, bob_priv, prime)

alice_shared = shared_key(bob_pub, alice_priv, prime)
bob_shared = shared_key(alice_pub, bob_priv, prime)

print("Alice public =", alice_pub)
print("Bob public =", bob_pub)
print("Alice shared =", alice_shared)
print("Bob shared =", bob_shared)

print("Keys match!" if alice_shared == bob_shared else "Keys differ!")
