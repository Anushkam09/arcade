import rock_paper_scissors
import numberguessing
import QuizGame
import MadLibs
import PIGgame
import hangman
import cowsandbulls
import sys

def arcade():
    def play():
        print("\n\n🎮 Welcome to the Arcade 🎮".center(50, "-"))
        print("1. Number Guessing Game".ljust(30, "."))
        print("2. Rock Paper Scissors".ljust(30, "."))
        print("3. Quiz Game".ljust(30, "."))
        print("4. MadLibs".ljust(30, "."))
        print("5. PIG Game (Multiplayer)".ljust(30, "."))
        print("6. Hangman".ljust(30, "."))
        print("7. Cows and Bulls".ljust(30, "."))
        print("8. Quit the Arcade".ljust(30, "."))

        try:
            playerchoice = int(input("\nEnter your choice: "))
            
            if playerchoice < 1 or playerchoice > 8:
                raise ValueError("🚫 Invalid choice")
            
            def maingame():
                if playerchoice == 1:
                    num_guess_game = numberguessing.numguess()
                    if num_guess_game == 1:
                        print("🥳 You win!")
                    else: 
                        print("🐍 Python wins")
                        
                elif playerchoice == 2: 
                    rps = rock_paper_scissors.rps()
                    if rps == 1:
                        print("🥳 You win!")
                    elif rps == 2: 
                        print("🐍 Python wins")
                    else:
                        print("🤝 Tie Game")
                        
                elif playerchoice == 3:
                    score = QuizGame.quiz_game()
                    print(f"Your final score is {score} 📝")
                    
                elif playerchoice == 4:
                    MadLibs.play()
                    print("\nThanks for your input in the story, it was interesting! 📖")
                    
                elif playerchoice == 5:
                    PIGgame.play()
                    
                elif playerchoice == 6:
                    hangman.hangman()
                    
                elif playerchoice == 7:
                    cowsandbulls.play()
                    
                elif playerchoice == 8:
                    sys.exit("👋 Thank you for visiting the arcade. Goodbye!")
                    
            maingame()
        
        except ValueError:
            print("🚫 Invalid input. Please enter a number between 1 and 8.")
            play()
            return

        print("\nPlay in the arcade again? 🥺")
        while True: 
            playagain = input("Enter Y for yes or N for No: ")
            if playagain.lower() not in ["y", "n"]:
                print("❗ Choose either Y or N")
            else: 
                break
        
        if playagain.lower() == "y":
            return play()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing! 👋")
            sys.exit("Bye! 👋")
    
    play()

arcade()
