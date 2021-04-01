import math, timeit
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
def twice(f,x):
    return f(f(x))

def expmod1(a,n,m):
    return (a ** n) % m

def expmod2(a,n,m):
    t=1
    for x in range(n):
        t=t*a % m

    return t

def expmod3(a,n,m):
    if n == 0:
        return 1
    else:
        d=expmod3(a,math.floor(n/2),m)
        if n % 2 ==0:
            return (d*d) % m
        else:
            return (d*d*a) % m

def probablePrime(n):
    return expmod3(2,n-1,n)
