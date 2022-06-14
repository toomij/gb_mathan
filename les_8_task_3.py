from scipy.optimize import fsolve, broyden2
import math

def equations(p):
    x, y = p
    # Запись системы уравнения вида x+y=2, x-y=0
    return (x*x-y*y+3*x*y*y*y-2*x*x*y*y+2*x-3*y-5, 3*y*y*y-2*x*x+2*x*x*x*y-5*x*x*y*y+5)

# Численное решение системы уравнений
x, y =  fsolve(equations, (10, 10))

print (x, y)