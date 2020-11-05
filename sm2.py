print("""
    1) Km a Millas marinas
    2) Millas marinas a Km
    3) Km a Millas terrestres
    4) Millas terrestres a Km
    5) Millas terrestres a Millas marines
    6) Millas marines a Millas terrestres
      """)
eligio = input("Que conversion quieres hacer ")
if eligio == "1":
  print("Has elegido convertir km a Millas marinas")
  km = float(input("Dime los km "))
  print("El resultado es: " , km * 0.539957 , "mm")
elif eligio == "2":
  print("Has elegido convertir Millas marinas a km")
  mm = float(input("Dime las millas marinas "))
  print("El resultado es: " , mm * 1.852 , "km")
elif eligio == "3":
  print("Has elegido convertir km a millas terresteres")
  km = float(input("Dime los km: "))
  print("El resultado es: " , km * 0.621371 , "mt")
elif eligio == "4":
  print("Has elegido convertir millas terrestres a km")
  mt = float(input("Dime las millas terrestres: "))
  print("El resultado es: " , mt * 1.60934 , "km")
elif eligio == "5":
  print("Has elegido convertir millas terrestres a millas marinas")
  mt = float(input("Dime las millas terrestres: "))
  print("El resultado es: " , mt * 0.868976 , "mm")
elif eligio == "6":
  print("Has elegido convertir Millas marinas a Millas terrestres")
  mm = float(input("Dime las Millas marinas: "))
  print("El resultado es: " , mm * 1.15078 , "mt")
else: 
  print("Esa opcion no existe")