## Creando un programa para acceder mediante una contraseña
pin=2475
intento=0
while intento <3:
    clave=int(input("Ingrese la clave del programa de Braykler: "))
    if clave == pin:
        print("Bienvenido al progrma de Braykler")
        break
    else:
        print (f"Clave incorrecta, le quedan {3 - intento -1} intentos")
        intento+=1
if intento == 3:
    print("Has agotado los 3 intentos, ¿Quién eres?")