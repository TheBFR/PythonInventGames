#This is a Guess the number game.
import random

guessTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName+  ', I am thinking of a number between 1 and 20.')

for i in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')
        guessTaken += 1

    if guess > number:
        print('You guess is too high.')
        guessTaken += 1

    if guess == number:
        guessTaken += 1
        break


if guess == number:
    guessTaken = str(guessTaken)
    print('Good job, '+myName+'! You guessed my number in ' + guessTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was '+number+'.')