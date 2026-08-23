import random

MIN_NUMBER = 1
MAX_NUMBER = 20


def welcome():
    """Print the welcome message and game instructions."""
    print("Welcome to this funny game!")
    print(f"I will guess a number between {MIN_NUMBER} and {MAX_NUMBER}, and")
    print("you have to guess it...")
    print("Go go go!")
    print()


def finish(number, count):
    """
    Print the end-of-round summary and ask if the user wants to play again.

    Args:
        number (int): The number the computer picked.
        count (int): How many guesses it took the user.

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """
    print("Good game!")
    print(f"My number was {number} and you found it in {count} guesses.")
    print()
    answer_input = input("Do you want to play again? (y/n): ")
    return answer_input.strip().upper() in ["Y", "YES"]


def win(computer_number, guess):
    """Return True if the guess matches the computer's number."""
    return computer_number == guess


def give_hint(computer, user):
    """Return a hint string comparing the user's guess to the computer's number."""
    if computer > user:
        return "My number is larger."
    if computer < user:
        return "Ohh... you went too large! Mine is smaller."
    return "Wow! You won! Good guess!"


def get_a_guess():
    """
    Ask the user for a guess and return it as an integer.
    Keeps asking until a valid integer is entered.
    """
    while True:
        raw_input_value = input("What is your guess? ")
        try:
            return int(raw_input_value)
        except ValueError:
            print("Please enter a valid whole number.")


def play_round():
    """Play a single round of the guessing game and return the guess count."""
    computer_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guess = 0
    count = 0

    while not win(computer_number, guess):
        guess = get_a_guess()
        count += 1
        print(give_hint(computer_number, guess))

    return computer_number, count


def main():
    """Run the main game loop."""
    welcome()
    continue_playing = True

    while continue_playing:
        number, count = play_round()
        continue_playing = finish(number, count)


if __name__ == "__main__":
    main()