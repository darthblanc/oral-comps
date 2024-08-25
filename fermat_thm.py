def super_mod(p, q, r):
    if q == 0:
        return 1
    elif q % 2 == 0:
        d = super_mod(p,q//2,r)
        return (d*d) % r
    else:
        d = super_mod(p,q-1,r)
        return (p*d) % r
        

if "__main__" == __name__:
    a = 28921829893273782737287387233376467346764364736473464
    b = 87382738784783748437487387487262376437644637473
    n = 892829828328738728
    print(super_mod(a, b, n))