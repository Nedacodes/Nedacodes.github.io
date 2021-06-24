#quadratic.py

import cmath 
a = int (input ('enter a: '))
b = int (input ('enter b: '))
c = int (input ('enter c: '))
def solve_quadratic(a,b,c):
    d = (b**2)-(4*a*c)
    if d < 0:
        return None
    if d == 0:
        solution1 = (-b + cmath.sqrt (d))/(2*a)
        return solution1 
    if d > 0:
        solution1 = (-b + cmath.sqrt (d))/(2*a) 
        solution2 = (-b - cmath.sqrt(d))/(2*a) 
        return (solution1, solution2)
print (solve_quadratic(a,b,c))
    


