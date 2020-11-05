dia = str(input("Dime el dia "))
mes = str(input("Dime el mes "))
año = str(input("Dime el año "))
if mes == "1" or mes == "3" or mes == "5" or mes == "7" or mes == "8" or mes == "10" or mes == "12" and dia >= "1" and dia < "32" and año <= "3000" and año >= "1":
  print("Es correcto")
elif mes == "2" and dia >= "1" and dia <= "28" and año <= "3000" and año >= "1": 
  print("Es correcto")
elif mes == "4" or mes == "6" or mes == "9" or mes == "11" and dia >= "1" and dia <= "30" and año <= "3000" and año >= "1":
  print("Es correcto")
else:
  print("No es correcto")