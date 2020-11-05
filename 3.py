import math
num1 = int(input("Pon el primer numero:\n"))
num2 = int(input("Pon el segundo numero:\n"))
num3 = int(input("Pon el tercer numero:\n"))
if num1 < num2 < num3:
  print(num1 , num2 , num3)
elif num3 < num2 < num1:
  print(num3 , num2 , num1)
elif num1 < num3 < num2:
  print(num1 , num3 , num2)
else:
  print(num2 , num3 , num1)