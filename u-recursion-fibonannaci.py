def fib_rec(n):

    if n <= 2:
        return 1

    return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(10))


def fib_dp(n, d = {}):
    print(d)    
    if n in d:
        print(f'n  = {n} is in the dictionary {d}')
        return d[n]

    if n<=2:
        return 1

    f = fib_dp(n-1) + fib_dp(n-2)
    print(f'n = {n}, f={f}')
    d[n] = f

    return f

print(fib_dp(10))

    

def fib_iterative(n):


    a=0
    b=1

    for i in range(n):
        a,b = b,a+b

    return a

print(fib_iterative(10))


