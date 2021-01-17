print("hola mundo, Bienvenidos a mi programa")

r = 3
a = 8

if r>=1 & r <=5:
    print("si entro al bucle")
    pass

if a==5 | a <= 3:
    print("si entro al segundo bucle")
    pass
else:
    print("no entro al segundo bucle")
    pass

p = 4^10

print('Este es p: '+ str(p))

q = not False

print(q)

e = 3 << 1

print("el desplazamiento es: "+ str(e))



continuar = True

while continuar == True:
    print("Hora vamos a probar una calcualdora: ")
    print("Ingrese el primer numero: ")
    numero1 = int(input())
    print("Ingrese el segundo numero: ")
    numero2 = int(input())


    print("Que operacion desea realizar?: \n1.suma 2.resta 3.multiplicacion 4.division ")
    option = input()

    if option == "1":
        suma = numero1 + numero2
        print("La suma es: " + str(suma))
        pass
    elif option == "2":
        resta = numero1 - numero2
        print("La resta es: " + str(resta))
        pass  
    elif option == "3":
        multiplicacion = numero1 * numero2
        print("La multiplicacion es: " + str(multiplicacion))
        pass
    elif option == "4":
        division = numero1 / numero2
        print("La division es: " + str(division))
        pass
    else:
        print("Opcion no valida")
        pass

    print("Desea continuar? 1.Si")
    option2 = int(input())
    if option2 == 1:
        continuar = True
        pass
    else:
        continuar = False
        pass
  

    pass



	


