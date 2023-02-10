print("Escoge la opción de lo qué quieres hacer")
print("1. Convertir Pesos a Dólares")
print("2. Convertir Dólares a Peso")
option = int(input("¿Qué quieres hacer? "))
trm = 4096
if option == 1 :
    pesos = int(input("Cuántos pesos colombianos tienes? "))
    print("Entonces tienes $" + str(round((pesos/trm),2)) + " dólares")
elif option == 2:
    dolares = int(input("Cuántos dólares tienes? "))
    trm = 4096
    print("Entonces tienes $" + str(round((dolares *trm),2)) + " pesos")
else:
    print("La opción seleccionada no es correcta")



