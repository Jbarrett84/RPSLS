from player import Player
from human import Human
import random

class Ai: 
    def __init__(self):
        self.name = "robo"
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.chosen_gesture) 
        print(f'{self.name} has picked {self.chosen_gesture}')
        
        

  