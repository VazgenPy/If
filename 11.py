dia = int(input("Dime el dia "))
mes = int(input("Dime el mes "))
año = int(input("Dime el año "))
hora = int(input("Dime la hora "))
minuto = int(input("Dime el minuto "))
segundo = int(input("Dime el segundo "))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
  if segundo == 59 and minuto !=59 and hora != 23:
    print(dia , mes , año , hora , minuto + 1 , segundo * 0)
  if segundo >= 0 and segundo <= 58: 
    print(dia , mes , año , hora , minuto , segundo + 1)
  if minuto == 59 and segundo == 59 and hora != 23:
    print(dia , mes , año , hora + 1 , minuto * 0 , segundo * 0)
  if hora == 23 and minuto == 59 and segundo == 59 and dia != 31:
    print(dia + 1 , mes , año , hora * 0 , minuto * 0 , segundo * 0)
  if dia == 31 and hora == 23 and minuto == 59 and segundo == 59 and mes != 12:
    print(dia - 30 , mes + 1 , año , hora * 0 , minuto * 0 , segundo * 0)    
  if mes == 12 and dia == 31 and hora == 23 and minuto == 59 and segundo == 59:
    print(dia - 30 , mes - 11 , año + 1 , hora * 0 , minuto * 0 , segundo * 0) 
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  if segundo == 59 and minuto != 59 and hora != 23:
    print(dia , mes , año , hora , minuto + 1 , segundo * 0)
  if segundo >= 0 and segundo <= 58: 
    print(dia , mes , año , hora , minuto , segundo + 1)
  if minuto == 59 and segundo == 59 and hora != 23:
    print(dia , mes , año , hora + 1 , minuto * 0 , segundo * 0)
  if hora == 23 and minuto == 59 and segundo == 59 and dia != 30:
    print(dia + 1 , mes , año , hora * 0 , minuto * 0 , segundo * 0)
  if dia == 30 and hora == 23 and minuto == 59 and segundo == 59:
    print(dia - 29 , mes + 1 , año , hora * 0 , minuto * 0 , segundo * 0)
elif mes == 2 and año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
  print("debug")
  if segundo == 59 and minuto != 59 and hora != 23:
    print(dia , mes , año , hora , minuto + 1 , segundo * 0)
  if segundo >= 0 and segundo <= 58: 
    print(dia , mes , año , hora , minuto , segundo + 1)
  if minuto == 59 and segundo == 59 and hora != 23:
    print(dia , mes , año , hora + 1 , minuto * 0 , segundo * 0)
  if hora == 23 and minuto == 59 and segundo == 59 and dia != 29:
    print(dia + 1 , mes , año , hora * 0 , minuto * 0 , segundo * 0)  
  if dia == 29 and hora == 23 and minuto == 59 and segundo == 59:
    print(dia - 28 , mes + 1 , año , hora * 0 , minuto * 0 , segundo * 0)
elif mes == 2 and año % 4 != 0 and año % 100 != 0 or año % 400 != 0:
  print("debug2")
  if segundo == 59 and minuto != 59 and hora != 23:
    print(dia , mes , año , hora , minuto + 1 , segundo * 0)
  if segundo >= 0 and segundo <= 58: 
    print(dia , mes , año , hora , minuto , segundo + 1)
  if minuto == 59 and segundo == 59 and hora != 23:
    print(dia , mes , año , hora + 1 , minuto * 0 , segundo * 0)
  if hora == 23 and minuto == 59 and segundo == 59 and dia != 28:
    print(dia + 1 , mes , año , hora * 0 , minuto * 0 , segundo * 0)
  if dia == 28 and hora == 23 and minuto == 59 and segundo == 59:
    print(dia - 27 , mes + 1 , año , hora * 0 , minuto * 0 , segundo * 0)    