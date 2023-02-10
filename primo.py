def es_primo(num):
    for n in range(2,int(num/2)):
        if num % n  == 0:
            return False
    return True


def run():
    #try:
    #numero = int(input("Por favor escribe un número para descubrir si es un número primo: "))
    numero = input("Por favor escribe un número para descubrir si es un número primo: ")
    assert numero.isnumeric(),"Debes ingresar un número entero"
    assert numero < 0,"Debe ser mayor que cero"
    numero = abs(int(numero))
    if es_primo(numero):
        print("El número " + str(numero) + ' es primo')
    else:
        print("El número " + str(numero) + ' no es primo')
    #except ValueError:
        print("Debes ingresar un número entero")

if __name__ ==  '__main__':
    run()
