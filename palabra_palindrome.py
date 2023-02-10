from math import ceil

def is_palindrome(word):
    lon = len(word)
    print(lon)
    cant = 0
    range_word = range(0, lon)
    for i in range_word:
        if word[i] != word[lon-(i+1)]:
            return False
        cant += 1
        print(cant)
    return True

def es_palindrome(word):
    k = len(word)
    lon = int(ceil(len(word)/2.0))
    print(lon)
    cant = 0
    range_word = range(0, lon)
    for i in range_word:
        if word[i] != word[(k-(i+1))]:
            return False
        cant += 1
        print(cant)
        #i = 10
    return True

word = input("Digite una palabra: ")
result = es_palindrome(word)
print("La palabra %s es %s" %(word, 'palindrome' if result else 'no palindrome'))
