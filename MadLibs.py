class InvalidChoice(Exception):
    pass

def play():
    print("\nWelcome to MadLibs game. \nYou need to select a story line out of the given stories.\nThen you will be given prompts to complete the storyline.\nAt the end, the entire story will be displayed to you.")
    print("\n\nHere are your story options:\n1. A day at the beach. \n2. The spooky haunted house. \n3. The Magical Forest Adventure \n4. The Alien Encounter \n5. The Great Cooking Disaster")
    def choices():
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2, 3, 4, 5]:
                raise InvalidChoice("This choice is not valid.")
        except ValueError:
            print("You should enter a number.")
            choices()
        except Exception as error:
            print(error)
            choices()
        return choice 
    
    def madlibs(content):
        story = ""
        i = 0
        while i < len(content):
            if content[i] == "<":
                word = ""
                j = i + 1
                while j < len(content) and content[j] != ">":
                    word += content[j]
                    j += 1
                if j < len(content):  
                    user_input = input(f"Enter a(n) {word}: ")
                    story += user_input
                    i = j + 1
                else:
                    story += "<" + word 
                    i = j
            else:
                story += content[i]
                i += 1
        print("\nYou've completed the story. Here it is: \n")
        print(story)    
    
    choice = choices()
    match choice:
        case 1:
            with open("dayatthebeach.txt") as f:
                content = f.read()
                madlibs(content)
        case 2:
            with open("spookyhouse.txt") as f:
                content = f.read()
                madlibs(content)
        case 3:
            with open("magicalforest.txt") as f:
                content = f.read()
                madlibs(content)
        case 4:
            with open("alienencounter.txt") as f:
                content = f.read()
                madlibs(content)
        case 5:
            with open("cookingdisaster.txt") as f:
                content = f.read()
                madlibs(content)
    
if __name__ == "__main__":
    play()