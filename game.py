#!/usr/bin/python3

import random
import time
import sys

print("Game Rules: ")
print("================================================================")
print("************ W E L C O M E  T O  M A N N I E V I L L E***********")
print("- A random team is generated and scrambled, giving you three(3) opportunities to guess the correct name. If the team is not guessed correctly, you lose. ")
print("Only authorised players are allowed to play the game ...")
print("***The PASSWORD is password*** \n")
print("================================================================")
print("\n")
time.sleep(1)


def validation():
    # Authentication
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if password == "password":
        print("Authenticating, please wait...")
        time.sleep(2)
        print("Good Luck ! ", username)
    else:
        sys.exit("Password is incorrect")


validation()
time.sleep(1)
print("\n")
# A list of spanish league teams
laLiga = [
    "Barcelona",
    "Osasuna",
    "Real Madrid",
    "Real Betis",
    "Granada",
    "Getafe",
    "Marloca",
    "Sevilla",
    "Villareal",
    "Levante",
]

print(laLiga)
print("\n")

# Choosing a random team
word = random.choice(laLiga).lower()
correct = word

print("Let's play...!!!")


new_word =""
count = 0
count2 = 3

# Create a scrambled version of the word
while word:
    position = random.randrange(len(word))
    new_word += word[position]
    word = word[: position] + word[(position + 1):]

print ("The team name is:", new_word)
 
guess = input("\nGuess your team name: ")
guess = guess.lower()

while count < 3 and (guess != correct) and (guess != ""):
    count += 1

    if guess not in correct and guess not in "":
        count2 -=1
        # if the character doesn’t match the word
  
        print("Sorry thats not the answer")

        # this will print the number of
        # turns left for the user
        print("You have ",  count2 ,"guesses left")
        guess = input("Your guess: ")
        guess = guess.lower()

    if guess == correct:
        print ("Yes!, you rock!\n")
    elif count == 3:
        print ("Thanks for playing, try again")
        print("The correct answer was: ", correct.upper())
 
input("\n\nPress the enter key to exit.")
       
