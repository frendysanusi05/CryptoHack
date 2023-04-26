# 11 ≡ x mod 6
# 8146798528947 ≡ y mod 17

# a ≡ b mod m <=> a mod m = b
def mod1(a, m):
    return a % m
    
x = mod1(11, 6)
y = mod1(8146798528947, 17)

print(min(x,y))