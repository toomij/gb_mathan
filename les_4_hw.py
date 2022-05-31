# На языке Python предложить алгоритм вычисляющий численно предел последовательности lim n/ n!**1/n
import math
from math import lgamma # lgamma(n) = ln((n-1)!)
import numpy as np
from decimal import Decimal
import time

# Через встроенный факториал

start_time = time.time()

def f(n):
    b = math.factorial(n)
    a = n / b**(1 / n)
    return a

acc = 0.0001
i = Decimal(2)

while(abs(f(i) - f(i - 1))) > acc:
    i += 1
print(f(i), abs(f(i) - f(i - 1)), i)
print("------ %s seconds ----" % (time.time() - start_time))

# Через самописный факториал
start_time = time.time()

acc = 0.00001
fact = Decimal(2)
i = Decimal(3)
fi_1 = 1 / 1 ** (1 / 1)
fi = 2 / 2 ** (1 / 2)

while (abs(fi - fi_1)) > acc:
    fact *= i
    fi_1 = fi
    fi = float(i / fact ** (1 / i))
    i += 1

print(f(i), abs(f(i) - f(i - 1)), i)
print("--- %s seconds ---" % (time.time() - start_time))



#Через формулу Стирлинга
start_time = time.time()

def f(n):
    return np.e/(2*np.pi*n)**(1 / (2 * n))
acc = 0.00000000001
i=2
while(abs(f(i)-f(i-1)))>acc:
    i +=1
print(f(i), abs(f(i)-f(i-1)), i)
print("--- %s seconds ---" % (time.time() - start_time))

#Через функцию lgamma(n) = ln((n-1)!)
start_time = time.time()

def f(n):
    return n/np.e**(lgamma(n + 1) / n)
acc = 0.00000000001
i=2
while(abs(f(i) - f(i-1))) > acc:
    i +=1
print(f(i), abs(f(i)-f(i-1)), i)
print("--- %s seconds ---" % (time.time() - start_time))