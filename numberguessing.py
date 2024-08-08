import sys
import random

def numguess():
    def play():
        print("\nWelcome to Number Guessing Game.\n")
        print("Guess a number from: 1, 2, 3, 4, 5\n")
        print("If you chose the same num as Python, you win.")
        player = int(input("\nEnter choice: \n"))
        if player not in [1,2,3,4,5]:
            print("Invalid choice")
            play()
                
        computer = int(random.choice("12345"))
        
        if player == computer: 
            return 1
        else:
            print(f"Oh no! Python chose {computer}")
            return 2
        
    return play()

if __name__ == "__main__":        
    print(numguess())
