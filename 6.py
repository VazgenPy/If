pp = int(input("Pon el precio que has pagado\n"))
po = int(input("Pon el precio original\n"))
dp = str(input("Quieres descontar?\n"))
if dp == "si":
  print("El porcentaje de descuento es:\n" , (pp/po)*(100)-100 , "%")
elif dp == "no":
  print("El precio descontado es:\n" , po-pp , "€")