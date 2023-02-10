def es_palindrome(cadena):
    cadena = cadena.replace(" ","").lower()
    print(cadena)
    if cadena == cadena[::-1]:
        print("La palabra o frase \"" + frase + "\"" + " es palíndrome")
    else:
        print("La palabra o frase \"" + frase + "\"" +" no es palíndrome")
frase = input("Escribe una palabra o frase: ")
es_palindrome(frase)