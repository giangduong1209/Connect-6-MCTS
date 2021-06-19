from board import *
import numpy as np 
SIZE = 21
B, W, EMPTY, EDGE = 1, -1, 0, 2
class Constant:
    def __init__(self, player):
        self.player = player
    def Opponent(self):
        if(self.player == 1):
            self.player = 0 
        else:
            self.player = 1 
        return self.player