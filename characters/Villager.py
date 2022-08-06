
import WinConditions as wc

class Villager(wc):
    
    def __init__(self):
        self.win = False
    
    def win_condition(self):
        print("Town Wins!!!!")
