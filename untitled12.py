#Barras de pan

pan = ("barra de pan")
precio_barra = float(3.49)
barra_no_vendida = int(input("Cantidad de barras no vendidas: "))
print ("El precio de una barra de pan es:",precio_barra)
monto_total_barras= float(precio_barra * barra_no_vendida)
descuento_barra = float((monto_total_barras * 60) / 100)
print ("El descuento de las barras de pan es de:",descuento_barra)
precio_final = float(monto_total_barras - descuento_barra)
print ("El precio final de las barras con el descuento es de:",precio_final)
