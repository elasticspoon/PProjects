def divisionAlg(n, d):
    q = 0
    while( (n - d) >= 0):
        n = n - d
        q += 1
    return (q, n)

print "GCD of:"
num1 = input("Enter Number 1:")
num2 = input("Enter Number 2:")

def euclid(a, b):
    if (b > a):
        c = b
        b = a
        a = c
    r = b
    while (b != 0):
        r = divisionAlg(a, b)[1]
        a = b
        b = r
    return a

print "GCD is: %d" % euclid(num1, num2)