from player import Player

class Human(Player):
    def __init__(self):
        self.name = ""
        self.set_name()
        super().__init__()

    def set_name(self):
       self.name = input("what is your name?")
        
    def choose_gesture(self):
        user_choice = int(input("enter 0 for rock, 1 for paper, 2 for scissor, 3 for lizard, 4 for spoke"))
        self.chosen_gesture = self.gestures[user_choice]
        print(f'{self.name} has chosen the gesture {self.chosen_gesture}')
