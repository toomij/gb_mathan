from sympy import *

init_printing()

x = Symbol('x')
f = x * sin(x)
print(diff(f, x))

x = Symbol('x')
f = x / sin(x)
print(diff(f, x))
