r = input("Enter Number:")
div = input("Enter Divisor:")

def divisionAlg(n, d):
    q = 0
    while( (n - d) >= 0):
        n = n - d
        q += 1
    return (q, n)

print "Qouteint: %d Remainder: %d" % divisionAlg(r, div)