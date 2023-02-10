from turtle import pos


# contador = 1
# numero = int(input("Digita un número que quieres elevar a una potencia: "))
# potencia = int(input("Ahora digita la potencia al que lo quiere elevar: "))
# while contador <= potencia:
#     print(str(contador) + ": " + str(numero) + " elevado a " + str(contador) + " es igual a " + str(pow(numero,contador)) )
#     contador += 1


# for contador in range(potencia+1) :
#     print(str(contador) + ": " + str(numero) + " elevado a " + str(contador) + " es igual a " + str(pow(numero,contador)) )

mult469 = [i for i in range(1,99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
mult469 = [i for i in range(1,99999) if i % 36 == 0]
print(mult469) 




# palabra = input("Escribe una palabra o frase: ")
# for letra in palabra:
#     if letra == " ":
#         break
#     print(letra)