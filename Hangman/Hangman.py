from faker import Faker

fake = Faker()

def clear_screen():
    print("\033[H\033[J", end='')

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
         -----
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / 
         -----
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |    
         -----
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    
           |    
         -----
        """,
        """
           ------
           |    |
           |    O
           |   \\|
           |    
           |    
         -----
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
         -----
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |    
         -----
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |    
         -----
        """
    ]
    return stages[tries]

def get_word():
    return fake.word().upper()

def play():
    word = get_word()
    word_letters = set(word)
    guessed_letters = set()
    guessed_wrong = set()
    tries = 7
    
    clear_screen()
    print("Welcome to Hangman!")
    
    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print(f"Wrong guesses: {' '.join(guessed_wrong)}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(f"Word: {' '.join(word_display)}")
        
        guess = input("Guess a letter: ").upper()
        if len(guess) < 2:
            if guess in guessed_letters or guess in guessed_wrong:
                print(f"You already guessed the letter {guess}. Try again.")
            elif guess in word_letters:
                guessed_letters.add(guess)
                word_letters.remove(guess)
            else:
                guessed_wrong.add(guess)
                tries -= 1
        else:
            print("You can max write 1 character.")
        
        clear_screen()
    
    if len(word_letters) == 0:
        print(display_hangman(tries))
        print(f"Congratulations! You guessed the word {word}.")
    else:
        print(display_hangman(0))
        print(f"Sorry, you ran out of tries. The word was {word}.")

if __name__ == "__main__":
    play()