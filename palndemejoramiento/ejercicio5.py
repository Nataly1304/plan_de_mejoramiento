"""
una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuanto debera pagar finalmente por su compra 
"""

precio = float(input("digite el precio compra:"))
descuento = precio * 0.15
precioTotal = precio - descuento 

print(f"el precio total a pagar es: {precioTotal:.2f} ")