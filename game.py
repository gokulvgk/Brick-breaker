import os
import time
import sys
class Board:
    def __init__(self):
        self.columns = 10
        self.rows = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.ballPos=self.columns//2
        self.fillBoard()

    def fillBoard(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if (row == 2 or row == 3) and 2 <= col <= self.columns - 3:
                    self.board[row][col] = '='
                elif row == 0 or col == 0 or col == self.columns - 1:
                    self.board[row][col] = '+'
                elif row == self.rows - 1:
                    self.board[row][col] = '_'
                else:
                    self.board[row][col] = ' '
        self.board[self.rows-1][self.columns//2] = 'o'

    def printBoard(self):
        os.system("clear")
        for row in self.board:
            print(''.join(row))
        time.sleep(0.5)
            
    def shootBall(self,direction):
        cmove={'st':0,'lt':-1,'rt':1}
        polarity=cmove[direction]
        ballr=self.rows - 1
        ballc=self.ballPos
        while not self.board[ballr - 1][ballc + polarity]=='=' and not ballr-1==0:
            if self.board[ballr - 1][ballc + polarity] == '+':polarity*=-1
            self.board[ballr - 1][ballc + polarity]='o'
            self.board[ballr][ballc]=' '
            ballr-=1
            ballc += polarity 
            self.printBoard()
        print("1st loop")
        if self.board[ballr -1][ballc + polarity]=='=':
            self.board[ballr -1][ballc + polarity]='o'
            self.board[ballr][ballc]=' '
            self.printBoard()
            ballr-=1
            ballc+=polarity
            polarity=0
        while ballr<self.rows-1:
            if self.board[ballr + 1][ballc + polarity] == '+':polarity*=-1
            self.board[ballr][ballc]=' '
            self.board[ballr + 1][ballc+polarity]='o'
            self.printBoard()
            ballr+=1
            ballc+=polarity
        self.ballPos=ballc
        self.newbase()
        self.printBoard()
    
    def newbase(self):
        self.board[-1] = ['_' if x == " " else x  for x in self.board[-1]]

b = Board()
b.printBoard()
while True:
    response = input("enter a direction to shoot: ")
    if response == 'x':sys.exit()
    b.shootBall(response)

