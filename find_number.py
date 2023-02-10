from random import randint
import os
def clear(): os.system('cls')

def findnumber():
    clear()
    print("""
    --- Find the number!!! ---
    Type a number between 1 and 100
    and let´s see how fast you are.""")
    picks = 0
    print(picks)
    number_to_find = randint(1,100)
    #print(number_to_find)
    num = -1
    while num != number_to_find:
        num = abs(int(input("\nPlease choose a positive number between 1 and 100: ")))
        if num < number_to_find:
            print("Choose a higher number")
            picks += 1
        elif num > number_to_find:
            print("Choose a lower number ")
            picks += 1
    print("¡¡Congratulations!!  You've found the number in " + str(picks) + " tries.")
    print("\nThis game is over")