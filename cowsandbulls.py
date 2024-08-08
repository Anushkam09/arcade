import random

class InvalidChoice(Exception):
    pass

def play():
    print("🐄🐂 Welcome to Cows and Bulls Game 🐂🐄")
    print("Rules: \n1. The computer will create a 5-digit random number with no repeated digits. \n2. The player has to guess the number. \n3. Upon making a guess, 2 hints will be provided - Cows and Bulls. \n4. Cows: correct digits and correct position. \n5. Bulls: correct digits but not at correct position. \n6. You will have 5 chances only.")
    print("Let's start! 🎉")
    
    chance = 0
    number = []
    while len(number) != 5:
        x = random.randint(0, 9)
        if x not in number:
            number.append(x)
    
    while chance != 5: 
        try:
            guess = input("Enter a 5-digit number to guess: ")
            if len(guess) != 5 or not guess.isdigit():
                raise InvalidChoice("🚫 Please enter a valid 5-digit number.")
            
            cows = 0
            bulls = 0
            cows_num = []
            bulls_num = []
            guess_list = [int(i) for i in guess]
            
            for i in range(5):
                if guess_list[i] == number[i]:
                    cows += 1
                    cows_num.append(guess_list[i])
                elif guess_list[i] in number and guess_list[i] not in cows_num:
                    bulls += 1
                    bulls_num.append(guess_list[i])
            
            if cows == 5:
                print("🎉 You've successfully guessed the number right!")
                return True
            
            print(f"🐄 COWS: {cows} numbers: {cows_num} \n🐂 BULLS: {bulls} numbers: {bulls_num}")
            chance += 1
            print(f"Chances Left: {5 - chance} 🔄")
        
        except InvalidChoice as error:
            print(error)
        
        except Exception:
            print("🚫 Enter a valid 5-digit number.")
    
    print("❌ Oh no! You've run out of chances.")
    num = ''.join(map(str, number))
    print(f"The correct number was: {num} 🔢")
    return False

if __name__ == "__main__":
    play()

