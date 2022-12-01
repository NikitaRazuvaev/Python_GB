''' f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
//    Определить корни
//    Найти интервалы, на которых функция возрастает
//    Найти интервалы, на которых функция убывает
//    Построить график
//    Вычислить вершину
//    Определить промежутки, на котором f > 0
//    Определить промежутки, на котором f < 0
'''

import matplotlib.pyplot as plt 

from sympy.solvers import solve
import sympy
import numpy as np

x = sympy.symbols('x')

f = -12*x**4*np.sin(np.cos(x)) - 188*x**3+5*x**2 + 10*x - 30
ans = sympy.solve(f)

print(ans)

