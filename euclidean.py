
def gcd(a, b):
    a, b = max(a, b), min(a,b)
    if b == 0:
        return a
    return gcd(b, a%b)

if "__main__" == __name__:
    print(gcd(5, 100))