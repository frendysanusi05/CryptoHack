# a^b % m
def mod_exp(a, b, m):
    if b == 0:
        return 1
    else:
        p = mod_exp(a, b//2, m) % m
        p = p*p % m
        if b%2 ==0:
            return p
        else:
            return a*p % m

if __name__ == '__main__':
    print(mod_exp(3,17,17))