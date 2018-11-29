#!/usr/bin/env pycal
Program := Fibonacci
# Fibonacci function written in pycal

def fibonacci(n) = 
    n:int
    if n <= 1 =
        return n
    else =  
        return fibonacci(n-1) + fibonacci(n-2)