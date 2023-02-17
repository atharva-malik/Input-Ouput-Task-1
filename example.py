import random  # Imports the random module used to generate random numbers

numGuesses = 0  # Keeps track of the number of guesses the user has made
randNum = random.randint(1, 100)  # Generates a random number between 1 and 100
while True:  # Runs the code forever
    userGuess = int(input("Guess a number between 1 and 100 (type STOP to stop): "))  # Asks the user to guess a number and turns it into a number
    numGuesses += 1  # Adds 1 to the number of guesses the user has made
    if int(userGuess) > randNum:
        print("Lower!")  # Tells the user that their guess was too high
    elif int(userGuess) < randNum:
        print("Higher!")  # Tells the user that their guess was too low
    elif int(userGuess) == randNum:
        print("You got it! It took you " + str(numGuesses) + " guesses.")  # Tells the user that they got it and how many guesses it took
        break
    else:
        print("Wrong input!")  # Tells the user that the input was wrong
