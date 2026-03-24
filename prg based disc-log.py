def prg(seed_val, prime, gen, size):
    state = seed_val % prime
    output_bits = []
    threshold = (prime - 1) // 2

    for _ in range(size):
        bit = 1 if state > threshold else 0
        output_bits.append(bit)
        state = pow(gen, state, prime)

    return output_bits


seed_val = int(input("Enter seed: "))
prime = int(input("Enter prime p: "))
gen = int(input("Enter generator g: "))
size = int(input("Enter output length: "))

bits = prg(seed_val, prime, gen, size)

print("Generated Bits:", "".join(map(str, bits)))
