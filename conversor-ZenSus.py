def conversor(moneda,monto):
    if moneda == "colombianos":
        trm = 4096
        print("Entonces tienes $" + str(round((monto/trm),2)) + " dólares")
    elif moneda == "mexicanos":
        trm = 24
        print("Entonces tienes $" + str(round((monto/trm),2)) + " dólares")
    elif moneda == "argentinos":
        trm = 65
        print("Entonces tienes $" + str(round((monto/trm),2)) + " dólares")
    elif moneda == "dolares":
        trm = 4096
        print("Entonces tienes $" + str(round((monto *trm),2)) + " pesos colombianos")



menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Dólares a pesos colombianos

Escoge una opción:
"""
option = int(input(menu))
monto = int(input("Escribe el monto: "))
if option == 1 :
    conversor("colombianos", monto)
elif option == 2 :
    conversor("mexicanos", monto)
elif option == 3 :
    conversor("argentinos", monto)
elif option == 4 :
    conversor("dolares", monto)
else:
    print("Lo siento. La opción seleccionada no es correcta")



