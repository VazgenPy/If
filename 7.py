import math
a = int(input("Dime el a  "))
b = int(input("Dime el b  "))
c = int(input("Dime el c  "))
print("El resultado positivo es: " , (-(b)+math.sqrt(b**2-4*a*c))/2*a)
print("El resultado negativo es: " , (-(b)-math.sqrt(b**2-4*a*c))/2*a)