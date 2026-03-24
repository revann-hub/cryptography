a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)
