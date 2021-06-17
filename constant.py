import numpy as np 
class Constant:
    def __init__(self, player):
        self.player = player
    def Opponent(self):
        if(self.player == 1):
            self.player = 0 
        else:
            self.player = 1 
        return self.player