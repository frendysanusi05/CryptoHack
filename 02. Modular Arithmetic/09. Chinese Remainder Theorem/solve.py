# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17

def findX(y, m, k):
    M = 1
    X = 0
    temp = 0
    Mi = [0]*k
    Z = [0]*k
    
    # Calculating M
    for i in range(k):
        M = M * m[i]
        
    # Calculating Mi
    for i in range(k):
        Mi[i] = M // m[i]
        
    # Calculating Zi
    for i in range(k):
        z = 0
        x = Mi[i]
        while((z * x) % m[i] != 1):
            z = z + 1
        Z[i] = z
        
    # Calculating X
    for i in range(k):
        temp = temp + (y[i] * Z[i] * Mi[i])
        
    # Final answer
    X = temp % M
    return X
    
y = [2, 3, 5]
m = [5, 11, 17]
k = len(y)
X = findX(y, m, k)
print(X)
# 872