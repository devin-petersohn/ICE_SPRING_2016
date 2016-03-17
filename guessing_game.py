#guessingGame
import random

number = random.randint(1,20)

print('Hello! What is your name?')
myName = input()

print("Well " + myName + " I'm thinking of a number between 1 and 20")
guess = 0
num_guesses = 5

while num_guesses > 0:
    print("Make a guess! " + str(num_guesses) + " guesses left!")
    guess = int(input())
    if guess < number:
        print("Too low!")
    if guess > number:
        print("Too high!")
    if guess == number:
        break
    num_guesses = num_guesses - 1

if guess == number:
    print("You win!")
if num_guesses == 0:
    print("You lost, I was thinking of " + str(number))
