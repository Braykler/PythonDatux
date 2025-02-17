### EJERCICIO 8
## Escriba un programa que pida un número entero y calcule la suma desde 1 hasta el número ingresado

a=int(input("Ingrese un número: "))
b=a*(a+1)//2
print("La suma es:", b)

## De otro modo

b=0
a=int(input("Ingrese un número: "))
for i in range(1, a+1):
    print(i)
    b=b+i
print("La suma es ",b)

