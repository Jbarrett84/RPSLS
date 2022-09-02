from human import Human
from ai import Ai

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None

    def run_game(self):
        self.welcome_message()
        self.choose_player()
        self.play()
        self.announce_winner()

    def welcome_message(self):
        print("welcome to rock paper scissor lizard and spoke. Here are the rules. Each player picks a variable and reveals it at the same time. The winner is the one who defeats the others. In a tie, the process is repeated until a winner is found. Good Luck.")

    def choose_player(self):
        user_choice = input("press 1 for single player or 2 for multiple players ")
        if user_choice == "1":
           self.player_one = Human()
           self.player_two = Ai()
        elif user_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
        

    def play(self):
        for number in range(2):
            print(number)
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("you picked the same gesture. Its a tie. choose again to keep playing")
        elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "scissor":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "rock" and self.player_two.chosen_gesture == "lizard":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "rock":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "paper" and self.player_two.chosen_gesture == "spock":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "scissor" and self.player_two.chosen_gesture == "paper":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "scissor" and self.player_two.chosen_gesture == "lizard":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture == "paper":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "lizard" and self.player_two.chosen_gesture == "spock":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture == "scissor":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        elif self.player_one.chosen_gesture == "spock" and self.player_two.chosen_gesture == "rock":
            print(f'{self.player_one.name} has won this round')
            self.player_one.wins += 1
        else:
             print(f'{self.player_two.name} wins this round') 
             self.player_two.wins += 1
        
        


    def announce_winner(self):
        if self.player_one.wins == 1:
            print("player one has won this round")
        elif self.player_two.wins == 1:
            print("player two has won this round")