import sys
import random

class InvalidChoice(Exception):
    pass

def play():
    print("\n\n🎲 Welcome to PIG Game 🎲\nThis is a multiplayer game.\n\n📜 Rules:\n1. You need to select the number of players and a target.\n2. The game is turn-based. Initial score will be 0 for all.\n3. The computer will roll a dice, and if the number is between 2 and 6, then the number will be added to the score.\n4. However, if 1 comes up, then your score will become 0, and the chance will be passed to the next player.\n5. The current player can roll the dice until they choose no, then the chance will be given to the next player.\n6. The player to reach the target first will win.\n7. To quit the whole game in the middle, press q.\n")

    def num_players():
        try:
            players_num = int(input("Enter number of players: "))
            if players_num < 2:
                raise InvalidChoice("Minimum 2 players required.")
        except ValueError:
            print("⚠️ You should enter a number.")
            return num_players()
        except InvalidChoice as error:
            print(f"⚠️ {error}")
            return num_players()
        return players_num
    
    def get_target():
        try:
            target = int(input("Enter your target: "))
            if target < 2:
                raise InvalidChoice("Enter a bigger target.")
        except ValueError:
            print("⚠️ You should enter a number.")
            return get_target()
        except InvalidChoice as error:
            print(f"⚠️ {error}")
            return get_target()
        return target

    players_num = num_players()
    target = get_target()
    scores = [0] * players_num
    players_list = []

    for i in range(players_num):
        name = input(f"Enter name of player {i + 1}: ")
        players_list.append(name)

    def continue_game():
        try:
            choice = input("Want to continue (y/n): ")
            if choice not in ["Y", "N", "y", "n", "Q", "q"]:
                raise InvalidChoice("Enter valid choice.")
            if choice in ["Y", "y"]:
                return True
            elif choice in ["Q", "q"]:
                sys.exit("🚪 You quit the game.\n👋 Bye bye!!\n\n")
            else:
                return False
        except InvalidChoice as error:
            print(f"⚠️ {error}")
            return continue_game()

    current_player_index = 0
    print("🎮 Game starts!")

    while True:
        current_player = players_list[current_player_index]
        print(f"\n🎲 Chance of {current_player}")
        print("Rolling the dice...")
        num_got = random.randint(1, 6)
        print(f"🎲 Dice shows: {num_got}")

        if num_got == 1:
            print(f"\n😢 OH no! You got 1.\nYour score is now 0\n")
            scores[current_player_index] = 0
            current_player_index = (current_player_index + 1) % players_num
        else:
            scores[current_player_index] += num_got
            print(f"🎉 You got {num_got}, now your score is {scores[current_player_index]}")

            if scores[current_player_index] >= target:
                print(f"\n\n🏆 We have a winner: {current_player}\n🎉 Congratulations!!")
                print("🎉 Thank you all for playing! 👋")
                break

            if not continue_game():
                current_player_index = (current_player_index + 1) % players_num

if __name__ == "__main__":
    play()
