from math import floor, sqrt

def is_prime(number):
    for factor in range(2, floor(sqrt(number))+1):
        if number % factor == 0:
            return False
    return True

if "__main__" == __name__:
    limit = 100 # change this to set the limit for the primes you want
    count = 0
    num = 2
    primes = []
    
    # this is a simple problem from number theory
    # we can use the fact that you only need to go up to the square root of a number to find all its factors
    # think about why?
    
    while count < limit:
        if is_prime(num):
            count += 1
            primes.append(num)
        num += 1
    
    print(count,'\n',primes)
    
    # alternatively, I was thinking of using the sieve of erathostenes
    # for that approach you need to have a movable ceiling that you can move until count n primes