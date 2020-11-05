print("""
    1) Dados 
    2) Nada
    """)
eligio = str(input("Que quieres hacer "))
if eligio == "1":
  numero = str(input("Dime que te ha salido en el dado "))
  if numero == "1":
    print("Te ha salido el numero uno")
    print("Y el numero de detras es: " , 7-1)
  elif numero == "2":
    print("Te ha salido el numero dos")
    print("Y el numero de detras es: " , 7-2)
  elif numero == "3":
    print("Te ha salido el numero tres")
    print("Y el numero de detras es: " , 7-3) 
  elif numero == "4":
    print("Te ha salido el numero cuatro")
    print("Y el numero de detras es: " , 7-4)
  elif numero == "5":     
    print("Te ha salido el numero cinco")
    print("Y el numero de detras es: " , 7-5)
  elif numero == "6":
    print("Te ha salido el numero seis")
    print("Y el numero de detras es: " , 7-6)
  else:
    print("El valor introducido no es valido")
elif eligio == "2":
  print("No quieres hacer nada")
else:
  print("Esa opcion no existe")