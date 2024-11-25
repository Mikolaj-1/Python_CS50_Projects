import random

def main():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if 1 <= level <= 100:
            break
        else:
            print("Please enter a level between 1 and 100.")

    number = random.choice(range(1, level + 1))

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if isinstance(guess, int):
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break

main()