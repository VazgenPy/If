import random
partidas = int(input("Cuantas partidas quieres jugar: "))
nombre = str(input("Dime tu nombre: "))
victorias = 0
derrotas = 0
while True:
  print("""
      1) Parells
      2) Senars
      """)
  quiere = int(input("Que quieres: "))
  numero = int(input("Que numero entre el 1 y el 9 eliges: "))
  ordenador = random.randint(1, 9)
  if quiere == 1:
    if (numero + ordenador) % 2 == 0:
      print("Has ganado " + nombre)
      victorias += 1  
    elif (numero + ordenador) % 2 != 0:
      print("Has perdido " + nombre)
      derrotas += 1
  elif quiere == 2:
    if (numero + ordenador) % 2 == 0:
      print("Has perdido " + nombre)   
      derrotas += 1
    elif (numero + ordenador) % 2 != 0:
      print("Has ganado " + nombre) 
      victorias += 1
  print("la maquina ha elegido: " , ordenador)
  print("La suma es: " , numero + ordenador)
  print("-----------------------------------------")
  if victorias + derrotas >= partidas:
    print("Has ganado" , victorias)
    print("Has perdido" , derrotas)
    break