dia = int(input("Dime el dia "))
mes = int(input("Dime el mes "))
año = int(input("Dime el año "))
if año <= 9999 and año >= 1:
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia >= 1 and dia <= 31:
      print("La fecha es correcta")
    else:
      print("La fecha no es correcta")
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
      print("La fecha es correcta")
    else: 
      print("La fecha no es correcta")
  elif año % 4 == 0 and año % 100 != 0 or año % 400 == 0 and mes == 2: 
      if dia >= 1 and dia <=29:
        print("La fecha es correcta")
      else: 
        print("La fecha no es correcta")
  elif año % 4 != 0 and año % 100 != 0 or año % 400 != 0 and mes == 2: 
    if dia >= 1 and dia > 29:
      print("La fecha es correcta")  
  else:
    print("La fecha no es correcta")