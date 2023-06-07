"""""
hacer un programa para ingresar el radio de un circulo y se reporte su area 
y la longitud de la circunferencia 
"""""

import math # colocamos esta variable por que estamos importando el valor de pi que se necesita para el area
radio = float(input("radio->"))
area = math.pi * radio**2
longitud = 2 * math.pi * radio

print(f"el area es: {area:.3f}")
print(f"el longitud de la circunferencia es: {longitud:.3f}")
