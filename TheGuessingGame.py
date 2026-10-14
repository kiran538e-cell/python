# Number Guessing Game

secret = 42
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess a number (1-100): "))

    if guess < 1 or guess > 100:
        print("Invalid number! Try again.")
        continue                  #skip that step and dos'nt count

    attempts += 1

    if guess == secret:
        print("Congratulations! You guessed correctly.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:                                         #else block with the while loop run when 5 attempts are wrong 
    print("Game Over! You lost.")