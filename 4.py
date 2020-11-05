num1 = int(input("Pon el primer numero")) 
num2 = int(input("Pon el segundo numero"))
resultado = int(num1%num2)
print(num1%num2)
if resultado == 0:
  print("EL producte es igual a 0")
elif resultado > 0:
  print("El producte es mes gran que 0")
else:
  print("El producte es mes petit que 0")