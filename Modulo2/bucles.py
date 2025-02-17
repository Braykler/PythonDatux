flag=True
while flag:
    print("bucle infinito")
    valor=input("ingrese si desea S/N si desea continuar o terminar el programa: ")
    if valor.upper()=="N":
        #break
        flag=False

#segundo
anio=2001
while anio <=2010:
    if anio in [2005,2006]:
        pass
    else:
        print(f"Informes del año {anio}")
    if anio == 2010:
        print("Salida del bucle, año 2010")
    anio += 1
print("finalizando el programa")