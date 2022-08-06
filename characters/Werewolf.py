
import winConditions as wc

class Werewolf(wc):
    
    def __init__(self):
        self.win = False
    
    def win(self):
        wc.winConditions(["Werewolf"])
        
