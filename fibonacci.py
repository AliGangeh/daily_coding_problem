#coding problem by apple
#fib(n) returns nth term of the Fibonacci sequence

def Fibonacci (n):
    return int((((1+5**(1/2))/2)**n - ((1-5**(1/2))/2)**n) / 5**(1/2))

Fibonacci(13)
