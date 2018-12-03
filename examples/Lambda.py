#!/usr/bin/env python
Program := FunWithLambdas
    
double := lambda x = x * 2
square := lambda x = x * x
    
nums := [ 1, 2, 3, 4, 5]
num_list := list(map(lambda x: x * 2 , num_list))

print(double(5))
print(square(5))
print(num_list)