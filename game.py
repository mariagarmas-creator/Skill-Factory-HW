''''game guess the number'''

import numpy as np

number = np.random.randint(1, 101)  # random number between 1 and 100

# count of attempts
count = 0

while True:
    
    count += 1
    guess = int(input("Enter your guess (between 1 and 100): "))
    
    if guess < number:
        print("Your guess is too low. Try again.")
    elif guess > number:
        print("Your guess is too high. Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {count} attempts.")
        break