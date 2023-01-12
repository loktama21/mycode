#!/usr/bin/env python3
#Guessing number game
import random

try:
    i = 0
    maxGuess = 3
    maxNum = 11
    minNum = 1
    luckyNumber = random.randrange(minNum, maxNum)
    while i < maxGuess:
        guessNumber = int(input("Guess the lucky number between 1-10: \n"))
        i=i+1
        #Guess number need to be 1-10 range
        if guessNumber < maxNum and guessNumber >= minNum:
            if guessNumber == luckyNumber:
                print("Congrats! You correctly guess the lucky number which is ", luckyNumber)
                break
            elif guessNumber > luckyNumber:
                print("You guess high. You have " + str(maxGuess-i) + " chances left.")
            elif  guessNumber < luckyNumber:
                print("You guess low. You have " + str(maxGuess-i) + " chances left.")
        else:
            print("Your guess number is outside the range.")
#catch any exception error            
except:
    print("Something went wrong")
#Final message
finally:
    print("Thanks for playing number guessing game!")
