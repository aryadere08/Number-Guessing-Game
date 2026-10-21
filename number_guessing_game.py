import random


def play_game():
    print("\n" + "=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)

    print("\nSelect Difficulty:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-500, 5 attempts)")

    while True:
        try:
            choice = int(input("\nEnter your choice (1-3): "))

            if choice in [1, 2, 3]:
                break
            else:
                print("Please select 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Enter a number.")

    if choice == 1:
        maximum = 50
        attempts = 10
        difficulty = "Easy"
    elif choice == 2:
        maximum = 100
        attempts = 7
        difficulty = "Medium"
    else:
        maximum = 500
        attempts = 5
        difficulty = "Hard"

    secret_number = random.randint(1, maximum)
    remaining = attempts
    score = 0

    print(f"\nDifficulty: {difficulty}")
    print(f"Guess a number between 1 and {maximum}.")
    print(f"You have {attempts} attempts.")

    while remaining > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > maximum:
                print(f"Enter a number between 1 and {maximum}.")
                continue

            remaining -= 1

            if guess == secret_number:
                score = remaining * 10 + 50
                print("\nCongratulations! You guessed correctly!")
                print(f"Secret number: {secret_number}")
                print(f"Attempts used: {attempts - remaining}")
                print(f"Your score: {score}")
                break

            elif guess < secret_number:
                print("Too low! Try a bigger number.")
            else:
                print("Too high! Try a smaller number.")

            print(f"Attempts remaining: {remaining}")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    else:
        print("\nGame over! You have used all your attempts.")
        print(f"The correct number was {secret_number}.")
        print("Your score: 0")

    print("=" * 40)


while True:
    play_game()

    again = input("\nWould you like to play again? (yes/no): ")
    if again.strip().lower() not in ("yes", "y"):
        print("\nThank you for playing!")
        break