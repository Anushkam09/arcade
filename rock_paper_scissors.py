import sys
import random
from enum import Enum 
def rps():
    def play():
        class RPS(Enum):
            Rock= 1
            Paper = 2
            Scissors = 3  
        print("\n\nWelcome to Rock Paper Scissors".center(30, "-"))
        print("Rock".ljust(25, ".") + "1".rjust(5))
        print("Paper".ljust(25, ".") + "2".rjust(5))
        print("Scissors".ljust(25, ".") + "3".rjust(5))

        playerchoice = int(input("\nEnter your choice: "))
        
        if playerchoice not in [1,2,3]:
            print("Invalid choice")
            play()
            
        computerchoice = int(random.choice("123"))

        print("\nYou chose "+ str(RPS(playerchoice)).replace('RPS.', "") + ".")
        print("Python chose "+str(RPS(computerchoice)).replace('RPS.', "") + ".\n")
        def decidewinner():
            if playerchoice == 1 and computerchoice ==3:
                return 1
            elif playerchoice == 3 and computerchoice ==2:
                return 1
            elif playerchoice == 2 and computerchoice == 1:
                return 1
            elif playerchoice == computerchoice: 
                return 3
            else:
                return 2
            
        return decidewinner()
    return play()
    
        
if __name__ == "__main__":
    game = rps()
    print(game)