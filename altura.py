option = 0
while(option == 0 ):
    # /print("Por favor escribe tu altura")
    option = int(input("¿Cuál es tu altura? "))
    if option < 150 :
        print("Eres una persona de estatura baja")
    elif option > 170:
        print("Es una persona de estatura alta")
    else:
        print("Eres una persona de estatura media")