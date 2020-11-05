dia = int(input("Dime el dia "))
mes = int(input("Dime el mes "))
año = int(input("Dime el año "))
if dia <= 30 and dia >= 1 and mes <= 12 and mes >= 1 and año >= 1 and año <= 2020:
  print("Es correcto")
else:
  print("NO es correcto")