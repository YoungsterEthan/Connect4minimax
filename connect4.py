import numpy as np
from scipy.signal import convolve2d
import random
import time

class ConnectFour():
    def __init__(self):
        self.board = np.zeros((6,7), dtype= int)
        self.rows = 6
        self.columns = 7
        self.player1 = 1
        self.player2 = 2
        self.turn = 0
        self.holder = ' [0 1 2 3 4 5 6]'
        
        print(self.board)
        print(' ----------------')
        print(self.holder)

    
    def insertPiece(self, column):
        if self.turn % 2 == 0:
            piece = self.player1
        else:
            piece = self.player2

        for row in range(self.rows-1, -1, -1):
            if self.board[row,column] == 0:
                self.board[row,column] = piece
                break
        self.turn += 1
        
        print(self.board)
        print(' ----------------')
        print(self.holder)
        if self.checkWinner(piece):
            print(piece, "is the winner")
            return True
        return False

    # def miniMax(self)
        

    def checkWinner(self,player):
        horizontal_kernel = np.array([[ 1, 1, 1, 1]])
        vertical_kernel = np.transpose(horizontal_kernel)
        diag1_kernel = np.eye(4, dtype=np.uint8)
        diag2_kernel = np.fliplr(diag1_kernel)
        detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]

        for kernel in detection_kernels:
            if (convolve2d(self.board == player, kernel, mode="valid") == 4).any():
                return True
        return False


    def play(self):
        player= int(input("Enter column 0-6: "))
        while(not self.insertPiece(player)):
            player = int(input("Enter column 0-6: "))
            

lol = ConnectFour()
lol.play()











