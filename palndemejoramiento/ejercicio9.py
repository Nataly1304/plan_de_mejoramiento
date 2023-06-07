"""""
construir un programa que simule el funcionamiento de una calculadora que 
puede realizar las 4 operaciones aritmeticas basicas (suma, resta, multiplicacion
y division)el uso debe especificar la operacion con el primer caracter del nombre
de la operacion 
S,s-suma
R,r-resta
P,P,M,m-multiplicacion
D,d-division 
"""
numero1= float(input("digite un numero:"))
numero2= float(input("digite otro numero:"))
operacion= input("\ningrese la operacion:")

if operacion.upper()=='S':
    suma= numero1+numero2
    print(f"\nla suma es: {suma}")
elif operacion.upper()=='R':
    resta= numero1-numero2
    print(f"\nla resta es: {resta}")
elif operacion.upper()=='M' or operacion.upper()=='P':
    multiplicacion= numero1*numero2
    print(f"\nla multiplicacion es: {multiplicacion:.2f}")
elif operacion.upper()=='D':
    division= numero1/numero2
    print(f"\nla division es: {division}")
else:
    print("no es valida la operacion")






