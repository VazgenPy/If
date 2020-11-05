numero = int(input("Introduzca el número del DNI: "))
letra = "TRWAGMYFPDXBNJZSQVHLCKE"
if numero < 10000000 or numero > 99999999: print("El numero del DNI no es correcto")
else: print('La letra del DNI es: ', letra[numero%23])