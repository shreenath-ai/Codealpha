import random


#   HANGMAN GAME — CodeAlpha Internship Task 1#


WORDS = ["python", "hangman", "laptop", "science", "program"]

# Hangman visual stages (0 = no mistakes, 6 = game over)
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]


def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def hangman():
    """Main Hangman game function."""
    print("=" * 40)
    print("   Welcome to HANGMAN! 🎮")
    print("=" * 40)

    
    word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print(f"\nGuess the word! It has {len(word)} letters.\n")

    while incorrect_guesses < max_incorrect:
       
        print(HANGMAN_STAGES[incorrect_guesses])

        # Show current word state
        print(f"Word:    {display_word(word, guessed_letters)}")
        print(f"Wrong guesses left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print("-" * 40)

     
        guess = input("Enter a letter: ").lower().strip()

        
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter!\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter!\n")
            continue

        
        guessed_letters.add(guess)

        if guess in word:
            print(f"✅  Great! '{guess}' is in the word!\n")
            # Check if player has won
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_STAGES[incorrect_guesses])
                print(f"🎉  YOU WIN! The word was: '{word.upper()}'")
                print("=" * 40)
                return
        else:
            incorrect_guesses += 1
            print(f"❌  Wrong! '{guess}' is not in the word.\n")

    
    print(HANGMAN_STAGES[max_incorrect])
    print(f"💀  GAME OVER! The word was: '{word.upper()}'")
    print("=" * 40)


def main():
    while True:
        hangman()
        print()
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye 👋")
            break
        print()


if __name__ == "__main__":
    main()