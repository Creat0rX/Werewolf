
import WinConditions as wc

class Werewolf(wc):
    
    def __init__(self):
        self.win = False
    
    def win_condition(self):
        print("Werewolf Wins!!!!")
        
