import random   

number = random.randint(1, 10)

print("Guess the number (1 to 10)")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You guessed it!")
        break   # stop the game

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Too low! Try again.")
        
