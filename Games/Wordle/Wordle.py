import random
import nltk
from nltk.corpus import words

nltk.download('words')

valid_words = {word for word in words.words() if len(word) == 5}

def generate_random_word():
    return random.choice(list(valid_words))

def provide_feedback(guess, target_word):
    feedback = ['_' for _ in range(len(target_word))]
    target_word_used = list(target_word)

    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            feedback[i] = guess[i]
            target_word_used[i] = None  

    for i in range(len(guess)):
        if feedback[i] == '_' and guess[i] in target_word_used:
            feedback[i] = '?'  
            target_word_used[target_word_used.index(guess[i])] = None  

    return ''.join(feedback)

def main():
    target_word = generate_random_word()
    attempts = 5

    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 5 attempts.\n")

    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower()

        if len(guess) != 5 or not guess.isalpha():
            print("Please enter a valid 5-letter word.")
            continue

        if guess not in valid_words:
            print("That word is not in the English dictionary. Please try another word.")
            continue
        
        feedback = provide_feedback(guess, target_word)

        if guess == target_word:
            print(f"Congratulations! You've guessed the word: {target_word}")
            break
        else:
            print(f"Feedback: {feedback}")

        if attempt == attempts - 1:
            print(f"Sorry, you've used all attempts. The word was: {target_word}")

if __name__ == "__main__":
    main()