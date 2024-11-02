import random
import time
import os
import sys
from faker import Faker

fake = Faker()

def generate_text(text_length):
    try:
        if text_length.lower() in ["s", "short"]:
            chars = 100
        elif text_length.lower() in ["n", "normal"]:
            chars = 200
        elif text_length.lower() in ["l", "long"]:
            chars = 300
        elif text_length.lower() in ["xl", "xlong"]:
            chars = 600
        else:
            print("Invalid length type. Defaulting to 'Normal'.")
            chars = 200
        
        return fake.text(max_nb_chars=chars)
    except Exception as e:
        print(f"Error generating text: {e}")
        return "Error generating text."

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_char():
    try:
        if os.name == 'nt':  # For Windows
            import msvcrt
            return msvcrt.getch().decode('utf-8')
        else:  # For Unix-based systems
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    except Exception as e:
        print(f"Error reading character: {e}")
        return ''  # Return empty string on error

def typing_game():
    while True:
        print("Welcome to the Typing Speed Test Game!")
        
        try:
            # Get the length of the text from the user
            text_length = input("How long should the text be? (Short / Normal / Long / XLong): ")
            
            # Generate the random text
            random_text = generate_text(text_length)
            if "Error" in random_text:
                return  # Exit if there was an error generating text

            print("\n" + random_text + "\n")

            input("Press Enter to start...")
            clear_screen()
            start_time = time.time()
            
            user_input = []
            while True:
                clear_screen()
                print("Type the following text:\n")
                print(random_text)
                print("\nYour input:\n", end='')

                # Display the user input and highlight correct/incorrect characters
                for i in range(len(random_text)):
                    if i < len(user_input):
                        if user_input[i] == random_text[i]:
                            print(f"\033[92m{user_input[i]}\033[0m", end='')  # Green for correct character
                        else:
                            print(f"\033[91m{random_text[i]}\033[0m", end='')  # Red for incorrect character
                    else:
                        print(f"\033[93m{random_text[i]}\033[0m", end='')  # Yellow for remaining text

                print("\n")
                
                # Capture next character
                next_char = get_char()
                if next_char == '\r':  # Ignore Enter key press
                    continue
                if next_char == '\x08':  # Handle backspace key press
                    if user_input:
                        user_input.pop()
                else:
                    user_input.append(next_char)
                
                # Check if the user has typed enough characters
                if len(user_input) >= len(random_text):
                    break

            end_time = time.time()

            elapsed_time = end_time - start_time
            words_typed = len(user_input) / 5  # Average word length is 5 characters
            wpm = (words_typed / elapsed_time) * 60

            correct_chars = sum(1 for i in range(len(random_text)) if i < len(user_input) and user_input[i] == random_text[i])
            accuracy = (correct_chars / len(random_text)) * 100

            print(f"\nTime taken: {elapsed_time:.2f} seconds")
            print(f"Words per minute (WPM): {wpm:.2f}")
            print(f"Accuracy: {accuracy:.2f}%")
        
        except KeyboardInterrupt:
            print("\nTyping test interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    while True:
        typing_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thank you for playing! Goodbye!")
            break