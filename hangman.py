import random
import sys

class myError(Exception):
    pass

def levels(word_list):
    words = word_list.split(',')
    word_to_guess = random.choice(words).strip()
    word_to_guess = word_to_guess.lower()
    return word_to_guess

def print_word(word, display_list):
    for i in word:
        if i == " ":
            print(" ", end=" ")
        elif i in display_list:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print()

def game(word, display_list, chances):
    correct = set()
    while chances < 7:
        guess = input("🔤 Enter a single character to guess: ").strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input. Please enter a single letter.")
            continue
        
        if guess in display_list:
            print("🚫 You've already selected this letter.")
            continue
        
        if guess in word:
            print("✅ Correct guess!")
            display_list.append(guess)
            correct.add(guess)
        else:
            print("❌ Incorrect guess.")
            display_list.append(guess)
            chances += 1
        
        print_word(word, display_list)
        
        if all(letter in display_list or letter == " " for letter in word):
            print("🎉 Congratulations! You've guessed the word!")
            return

    print(f"💀 Game Over! The word was: {word}")

def print_Menu():
    print("🎮 Welcome to the Hangman Game! 🎮")
    print("You can only get 7 chances wrong for guessing a word (for each level).")
    print("📜 This has 3 levels:")
    print("1️⃣ Level 1: Fruits")
    print("2️⃣ Level 2: Movies")
    print("3️⃣ Level 3: Celebrities.")

def hangman():
    fruits = """apple, lychee, mango, banana, strawberry, peach, pineapple, apricot, coconut, guava, pear, blackberry, watermelon, muskmelon, raspberry, blueberry, grapefruit, grapes, avocado, plum, starfruit"""
    movies = """Ready, Phir Hera Pheri, Hera Pheri, Main tera hero, Humpty Sharma ki dulhania, Baby, Hey baby, Bhramastra, Kalki, Hum saath saath hain, Happy new year, Hum aapke hain kon, crew, mohabbatein, dishoom, baghban, Tarzan the wonder car, bajrangi bhaijaan, sultan"""
    celebrities = """Varun Dhawan, Anushka Sharma, Akshay Kumar, Shahrukh Khan, Salman Khan, Saif ali Khan, Sharddha Kapoor, Aditya Roy Kapoor"""
    
    print_Menu()
    
    
    def choice():
        try: 
            level = input("Choose a level (1️⃣ for Fruits, 2️⃣ for Movies, 3️⃣ for Celebrities, Q to quit): ")
            if level in "123qQ":
                return level
            else:
                raise myError("⚠️ Invalid Choice")
        except ValueError:
            print("⚠️ Invalid Input")
            return choice()
        except Exception as error:
            print(error)
            return choice()
    
    level = choice()
    
    if level == "1":
        word_list = fruits
    elif level == "2":
        word_list = movies
    elif level == "3":
        word_list = celebrities
    else:
        print("🚪 You quit the hangman game. 👋 Goodbye!")
    
    word = levels(word_list)
    print_word(word, [])
    game(word, [], 0)

if __name__ == "__main__":
    hangman()
