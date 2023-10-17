import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 100)

# Number of attempts allowed
attempts = 0

print("Welcome to the Random Number Prediction Game!")
print("I've chosen a number between 1 and 100. Try to guess it.")

while True:
    try:
        # Get the player's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# End of the game
print("Thanks for playing!")
