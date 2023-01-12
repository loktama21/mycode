import random

try:
    i = 0
    maxGuess = 3
    maxNum = 11
    minNum = 1
    while i < maxGuess:
        guessNumber = int(input("Guess the lucky number between 1-10: \n"))
        luckyNumber = random.randrange(minNum, maxNum)
        i=i+1
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
except:
    print("Something went wrong")
finally:
    print("Thanbks for playing guessing game!")
