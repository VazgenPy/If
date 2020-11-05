import random
partidas = int(input("Cuanta partidas quieres jugar? "))
victorias = 0 
derrotas = 0
while True:
  maquina = random.randint(1, 2)
  print("""
        1) Cara
        2) Cruz
        """)
  quiere = int(input("Que quieres: "))
  if quiere == 1: 
    print("Has elegido cara")     
    if maquina == 1:
      print("Ha salido cara, has ganado")
      victorias += 1
    elif maquina == 2:
      print("Ha salido cruz, has perdido")
      derrotas += 1 
  elif quiere == 2:
    print("Has elegido cruz") 
    if maquina == 2:
      print("Ha salido cruz, has ganado")   
      victorias += 1   
    elif maquina == 1:
      print("Ha salido cara, has perdido") 
      derrotas += 1
  print("-------------------------------------")  
  if victorias + derrotas >= partidas:
    print("Has ganado" , victorias) 
    print("Has perdido" , derrotas)  
    break