# cryptography
1. affine.py  
This script implements the Affine cipher, a classical substitution cipher based on modular arithmetic. It demonstrates how each letter of the alphabet can be transformed using a linear function and then mapped back to plaintext through modular inversion. The code highlights both encryption and decryption processes, showing how mathematical operations can secure text while also being reversible when the correct keys are known.

2. ceasar.py  
This program provides an implementation of the Caesar cipher, one of the simplest and most well‑known encryption techniques. It allows users to shift letters by a fixed number across the alphabet to produce ciphertext. The script also includes a frequency analysis function that can estimate the key by comparing letter distributions, illustrating both the cipher’s simplicity and its vulnerability to statistical attacks.

3. rsa.py  
This file contains a basic RSA cryptosystem implementation, including key generation, modular inverse calculation, and encryption/decryption of integer messages. It demonstrates how two large primes are used to construct the modulus, how Euler’s totient function is applied, and how modular arithmetic ensures secure communication. The script emphasizes the importance of choosing proper keys and validates inputs to prevent insecure configurations.

4. hellman.py  
This script illustrates the Diffie–Hellman key exchange protocol, where two parties generate public keys and compute a shared secret over an insecure channel. It shows how modular exponentiation enables secure key agreement without directly transmitting the secret. The code highlights the symmetry of the process, where both participants arrive at the same shared key, forming the basis of secure communication in modern cryptography.

5. gcd.py  
This program implements the Euclidean algorithm to compute the greatest common divisor (GCD) of two integers, as well as the extended version to find modular inverses. These functions are critical in cryptography, especially in RSA and other public‑key systems, where modular arithmetic requires coprime values. The script demonstrates the iterative process of reducing numbers until the GCD is found and how coefficients can be used to solve linear congruences.

6. frequency analys.py  
This file provides a simple frequency analysis tool for breaking substitution ciphers. It scans ciphertext, counts occurrences of letters, and identifies the most frequent symbol, which is often mapped to ‘E’ in English plaintext. The script demonstrates how statistical methods can be used to attack classical ciphers, highlighting the weaknesses of simple substitution techniques.

7. prg based disc-log.py  
This script implements a pseudo‑random generator (PRG) based on discrete logarithms. It uses modular exponentiation to produce sequences of bits that appear random but are deterministically generated from a seed. The code illustrates how number theory can be applied to generate cryptographic randomness, which is essential for secure key generation and encryption schemes.

8. prg+otp.py  
This program combines a pseudo‑random generator with the one‑time pad encryption scheme. It generates a key stream from a seed and uses XOR operations to encrypt and decrypt messages. The script demonstrates how PRGs can approximate the security of OTP when true randomness is unavailable, while also showing the limitations of deterministic key generation.

9. OTPP.py  
This file implements a one‑time pad encryption scheme using pseudo‑randomly generated keys. It highlights the XOR operation as the core of OTP, where plaintext and key are combined to produce ciphertext. The script emphasizes the importance of key length and uniqueness, showing how OTP can theoretically achieve perfect secrecy if keys are truly random and never reused.

10. CPA secure OTP.py  
This script explores the concept of CPA‑secure (Chosen Plaintext Attack secure) one‑time pad encryption. It demonstrates how randomness in key generation can protect against adversaries who attempt to exploit predictable patterns. The code provides an educational example of how OTP can be adapted to resist stronger attack models, reinforcing the principle that security depends on both algorithm design and randomness quality.`
