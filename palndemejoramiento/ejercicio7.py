# hacer un programa que pida 3 numeros y determine cual es el mayor 


numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese un tercer numero: "))

if numero1>=numero2 and numero1>=numero3:
    print(f"el numero mayor es:{numero1:.0f}")
elif numero2>=numero1 and numero2>=numero3:
    print(f"el numero mayor es:{numero2:.0f}")
elif numero3>=numero1 and numero3>=numero2:
    print(f"el numero mayor es:{numero3:.0f}")