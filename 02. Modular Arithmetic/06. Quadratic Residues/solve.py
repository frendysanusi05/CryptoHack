### We say that an integer x is a Quadratic Residue if there exists an a such that a^2 = x mod p. If there is no such solution, then the integer is a Quadratic Non-Residue.

p = 29
ints = [14, 6, 11]

for i in range(1, p):
    x = pow(i, 2, p)
    if (x in ints):
        print(f"x: {x}, i: {i}")
        