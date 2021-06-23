#quadratic.py

import cmath 
a = float (input ('enter a: '))
b = float (input ('enter b: '))
c = float (input ('enter c: '))
d = (b**2)-(4*a*c)
solution1 = (-b + cmath.sqrt (d))/(2*a) 
solution2 = (-b - cmath.sqrt(d))/(2*a) 
print ('solutions are: {0},{1}'.format(solution1,solution2))
