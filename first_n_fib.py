
if "__main__" == __name__:
    limit = 1000 # change this to set the limit for the fibonacci numbers you want
    fib = [0, 1]
    
    # this is a dynamic programming problem
    # the fibonacci sequence is defined as f[i] = f[i-1] + f[i-2]
    # as you can see the subproblems are well defined, so just solve the subproblems
    # I have implemented the approach using tabulation
    # you could attempt to solve it using memoization
    
    for i in range(2, limit+1):
        fib.append(fib[i-1] + fib[i-2])
    
    print(fib[limit], fib)