from turtle import pos


# contador = 1
# numero = int(input("Digita un número que quieres elevar a una potencia: "))
# potencia = int(input("Ahora digita la potencia al que lo quiere elevar: "))
# while contador <= potencia:
#     print(str(contador) + ": " + str(numero) + " elevado a " + str(contador) + " es igual a " + str(pow(numero,contador)) )
#     contador += 1


# for contador in range(potencia+1) :
#     print(str(contador) + ": " + str(numero) + " elevado a " + str(contador) + " es igual a " + str(pow(numero,contador)) )


palabra = input("Escribe una palabra o frase: ")
for letra in palabra:
    if letra == " ":
        break
    print(letra)