def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b%a, a)
        return gcd, y-(b//a)*x, x

if __name__ == '__main__':
    p = 26513
    q = 32321
    gcd, u, v = extended_gcd(p, q)
    print(min(u,v))