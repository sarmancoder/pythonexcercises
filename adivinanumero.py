from random import *

lownumber = 10
highnumber = 20
aleatorio = randint(lownumber, highnumber)
# print("Sumado uno " + str((numero + 1)))
print(f"Sumado uno {aleatorio + 1}")
# print("El numero que has escogido es: " + str(numero))

tries = 3
acierto = False

for i in range(0, tries):
    numero = int(input(f"Escoge un número entre {lownumber} y {highnumber}: "))
    if numero > aleatorio:
        print("El número es menor")
    elif numero < aleatorio:
        print("El numero es mayor")
    else:
        acierto = True
        print("¡Adivinaste el numero!")
        break;

if acierto == False:
    print(f"El numero era {aleatorio}")