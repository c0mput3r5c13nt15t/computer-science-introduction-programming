# Importieren des Moduls für das generieren von Zufallszahlen
import random


def input_choice(question: str, options: list[str]) -> str:
    """
    Asks the user a question and returns the answer if it is in the list of options. If the answer is not in the list of options, the question is asked again.
    """
    print(f"{question} [{' | '.join(options)}]")
    answer = input('> ')
    while answer not in options:
        print("Invalid answer. Try again.")
        answer = input('> ')
    return answer


def shape(word: str, guesses: str) -> str:
    word_shape = ""
    for letter in word:
        if letter in guesses:
            word_shape += letter
        else:
            word_shape += "_"
    return word_shape


def hangman(word: str, allowed_mistakes: int) -> None:
    """
    Play a round of hangman. The player has to input single letter guess until the word is guessed or the allowed number of mistakes is reached.
    """
    mistakes = 0
    guesses = ""
    while mistakes < allowed_mistakes:
        new_guess = input(
            f"{shape(word, guesses)}; {allowed_mistakes - mistakes} mistakes left; make a guess: ")
        if len(new_guess) != 1:
            print("Invalid input. Guess has to be exactly one letter. Try again.")
        elif new_guess in guesses:
            print("Invalid input. You already guessed that letter. Try again.")
        elif new_guess not in word:
            mistakes += 1
        elif new_guess in word:
            guesses += new_guess

            if shape(word, guesses) == word:
                print(
                    f"\nYou won! The word was '{word}'! You're the best! Everyone loves you!")
                return
    print(
        f"\nYou lost! The word was '{word}'! You're the worst! Everyone hates you!")
    return


if __name__ == '__main__':
    words = ['apple', 'tree', 'python', 'bench', 'float']

    max_fails = int(input("Number of allowed mistakes: "))

    while input_choice("Wanna play a game?", ['yes', 'no']) == 'yes':
        word = random.choice(words)  # Wähle ein zufälliges Wort aus.
        hangman(word, max_fails)
