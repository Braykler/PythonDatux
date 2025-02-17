print("Bienvenidos al primer menú realizado por Braylkler en Python")
while True:
    print("""OPCIONES DISPONIBLES EN EL MENU DE BRAYKLER
          1. Saludar
          2. Sumar dos números
          3. Saber si ella te ama
          4. Salir del programa""")
    opcion=int(input("Ingrese la opción que desea realizar: "))
    if opcion == 1:
        print("Hola, soy Braykler, bienvenido a mi primer menu en Python")
    elif opcion == 2:
        n1=int(input("Ingrese el primer número: "))
        n2=int(input("Ingrese el segundo número: "))
        resultado=n1+n2
        print("El resultado de la suma es: ",resultado)
    elif opcion == 3:
        print("Lo siento, ella no te ama")
    elif opcion == 4:
        print("Gracias por visitar mi menu, vuelve pronto.")
        break
    else:
        print("Ingrese una opción válida.")
    