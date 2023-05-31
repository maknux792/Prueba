texto=""
totaln=0
totalj=0
totala=0
totalf=0
cniños=0
personasf=0
cjovenes=0
cadultos=0
while texto !="fin":
    print("-----🌟Bienvenido al cine moro🌟-----")
    print("---------------------------------")
    print("Niños     [edad] 1-13      = $5500 ")
    print()
    print("Jovenes   [edad] 14-21     = $7000 ")
    print()
    print("Adultos   [edad] mayor a 22= $9000 ")
    print("=================================")

    edad=int(input("Ingrese su edad: "))
    if edad>= 1 and edad<= 13:

        print("Usted esta en la categoria de niños")
        cantidad=int(input("Ingrese cantidad de entradas: "))
        cniños=cantidad+cantidad
        cantidad=cantidad*5500
        totaln+=cantidad
        print(f"Cantidad a pagar: {cantidad}")
        texto=input("Siquiere finalizar escribir [fin] si no precione un caracter: ")
    
    elif edad>=14 and edad<=21:
        print("Usted esta en la categoria de jovenes")
        cantidad=int(input("Ingrese cantidad de entradas: "))
        cjovenes=cantidad+cantidad
        cantidad=cantidad*7000
        totalj+=cantidad
        print(f"Cantidad a pagar: {cantidad}")
        texto=input("Siquiere finalizar escribir [fin] si no precione un caracter: ")

    elif edad>=22:
        print("Usted esta en la categoria de adultos")
        cantidad=int(input("Ingrese cantidad de entradas: "))
        cadultos=cantidad+cantidad
        cantidad=cantidad*9000
        totala+=cantidad
        print(f"Cantidad a pagar: {cantidad}")
        texto=input("Siquiere finalizar escribir [fin] si no precione un caracter: ")

    if edad==0 and edad<0:
        print("La edad no esta dentro de los parametros😨")
print("==============================================")
print("Fin de la jornada")
print("-----------------")
totalf=totaln+totalj+totala
cantidadp=cniños+cjovenes+cadultos
porcentaje1=cniños*100/cantidadp
porcentaje2=cjovenes*100/cantidadp
porcentaje3=cadultos*100/cantidadp
print("Cantidad total de entradas vendidas en la jornada")
print("----------------------------------------")
print(f"Cantidad total de entradas de niños vendidas: ${totaln}")
print(f"Procentaje de entradas de niño vendida: {int(porcentaje1)}%")
print()
print(f"Cantidad total de entradas de niños vendidas: ${totalj}")
print(f"Procentaje de entradas de niño vendida: {int(porcentaje2)}%")
print()
print(f"Cantidad total de entradas de niños vendidas: ${totala}")
print(f"Procentaje de entradas de niño vendida: {int(porcentaje3)}%")
print()
print(f"Cantidad total de entradas vendidas en la jornada:${totalf}")
print("==========================================")
print("Hasta pronto😁")