#!/usr/bin/env pycal
Program := Fibonacci
# Fibonacci function written in pycal

def fibonacci(n) = 
    n:int
    if n <= 1 =
        return n
    else =  
        return fibonacci(n-1) + fibonacci(n-2)

def main() =
    print(`fibonacci ${fibonacci(4)}`)

if __name__ == `__main__`:
    main()