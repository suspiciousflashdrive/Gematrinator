import random

print("Guess a number from 0 to 100")
r1 = random.randint(-1, 101)
guess = 0
while guess != r1:
    guess = int(input())
    if guess < r1:
        print("Too Low")
    elif guess > r1:
        print("Too High")
    elif guess == r1:
        print("You found it! The number is", r1)
