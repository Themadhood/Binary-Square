#program:       Binary_Square
#purpose:       makes the board
#progamer:      Madison Arndt 7/26/2022

_FILE = "Binary_Square"
_VERSION = "0.0.1"

import random
random.seed()
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from THEMADHOOD.Library import Error
    
import os
FP = os.path.dirname(os.path.abspath(__file__))


def DivisibleByTwo(amount):
    try:
        divis = amount % 2
        if divis == 0:
            return True
    except Exception as e:
        Error.UploadError([_FILE,_VERSION,"","DivisibleByTwo",
                           f"failed devide {amount} by 2",e],"Small Apps")
    return False

class Binary_Square:
    def __init__(self):
        self._Error = False
        #creates the window
        self.window = Tk()
        self.window.iconbitmap(default = FP +"/Binery_Game_icon.ico")
        self.window.title("Binery Square")#title of widow
        self.window.config(bg='black')#collor

        #ask for size
        self.size = simpledialog.askinteger(" ","How Big? 5 - 20",
                                          parent=self.window,
                                          minvalue=5,maxvalue=20)
        change = self.size*2
        
        self.Hight = 28 * self.size + 3 + 30
        self.WITH = 28 * self.size + 3 #+ 800
        #size (X)x(Y) location  +(X)+(Y)
        self.window.geometry(f"{self.WITH}x{self.Hight}")
        
        binery = [0,1]
        #creates the board
        self.board = []
        Y = 0 + 3
        for i in range(0,self.size-1):
            self.board.append([])
            X = 0 + 3
            for j in range(0,self.size-1):
                space = random.randint(0,1)
                self.board[i].append(Space(self.window,binery[space],X,Y))
                
                X += 28
            Y += 28

        #virtical Check
        Y = 0 + 3
        for i in range(0,self.size-1):
            cont = 0
            X = 0 + 3
            for j in range(0,self.size-1):
                cont += self.board[i][j].anser
                X += 28
                
            if DivisibleByTwo(cont):
                self.board[i].append(Space(self.window,0,X,Y))
            else:
                self.board[i].append(Space(self.window,1,X,Y))
            Y += 28

        #horizontal Check
        X = 0 + 3
        btcont = 0
        self.board.append([])
        for i in range(0,self.size):
            cont = 0
            Y = 0 + 3
            for j in range(0,self.size-1):
                cont += self.board[j][i].anser
                Y += 28

            if DivisibleByTwo(cont) and i < self.size-1:
                self.board[self.size-1].append(Space(self.window,0,X,Y))
            elif not DivisibleByTwo(cont) and i < self.size-1:
                self.board[self.size-1].append(Space(self.window,1,X,Y))
                btcont +=1
            elif DivisibleByTwo(cont) and DivisibleByTwo(btcont):
                self.board[self.size-1].append(Space(self.window,0,X,Y))
            elif not DivisibleByTwo(cont) and not DivisibleByTwo(btcont):
                self.board[self.size-1].append(Space(self.window,1,X,Y))
            X += 28

        cwards = set()
        while change > 0:
            y = random.randint(0,self.size-1)
            x = random.randint(0,self.size-1)
            if (x,y) not in cwards:
                cwards.add((x,y))
                self.board[y][x].Empty()
                change -=1
            

        #bord vew var
        self.chk = Button(self.window,bg = "gray",fg = "black",
                   font = ('timesnewroman 9 bold'),
                   text = "Check",
               command=self.Check)
        
        self.chk.place(x=self.WITH-52,y=self.Hight-27)
        

    def Check(self):
        try:
            end = True
            fail=False
            playAgain = None
            for i in range(0,self.size):
                for j in range(0,self.size):
                    check = self.board[i][j].Correct()
                    if check == None:
                        end = False
                    elif not check:
                        fail = True

            if fail:
                playAgain = messagebox.askyesno('You Loose',
                                                 'Do you want to play again?')
            elif not fail and end:
                playAgain = messagebox.askyesno('You Win',
                                                 'Do you want to play again?')
            if playAgain and end:
                self.PlayAgain()
            elif not playAgain and end:
                self.window.destroy()
        
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Binary_Square","Check",
                               f"failed to check state",e],"Small Apps")

    def PlayAgain(self):
        try:
            #ask for size
            self.size = simpledialog.askinteger(" ","How Big? 5 - 20",
                                              parent=self.window,
                                              minvalue=5,maxvalue=20)
            change = self.size
            
            self.Hight = 28 * self.size + 3 + 30
            self.WITH = 28 * self.size + 3 #+ 800
            #size (X)x(Y) location  +(X)+(Y)
            self.window.geometry(f"{self.WITH}x{self.Hight}")
            
            binery = [0,1]
            #creates the board
            self.board = []
            Y = 0 + 3
            for i in range(0,self.size-1):
                self.board.append([])
                X = 0 + 3
                for j in range(0,self.size-1):
                    space = random.randint(0,1)
                    self.board[i].append(Space(self.window,binery[space],X,Y))
                    
                    X += 28
                Y += 28

            #virtical Check
            Y = 0 + 3
            for i in range(0,self.size-1):
                cont = 0
                X = 0 + 3
                for j in range(0,self.size-1):
                    cont += self.board[i][j].anser
                    X += 28
                    
                if DivisibleByTwo(cont):
                    self.board[i].append(Space(self.window,0,X,Y))
                else:
                    self.board[i].append(Space(self.window,1,X,Y))
                Y += 28

            #horizontal Check
            X = 0 + 3
            btcont = 0
            self.board.append([])
            for i in range(0,self.size):
                cont = 0
                Y = 0 + 3
                for j in range(0,self.size-1):
                    cont += self.board[j][i].anser
                    Y += 28

                if DivisibleByTwo(cont) and i < self.size-1:
                    self.board[self.size-1].append(Space(self.window,0,X,Y))
                elif not DivisibleByTwo(cont) and i < self.size-1:
                    self.board[self.size-1].append(Space(self.window,1,X,Y))
                    btcont +=1
                elif DivisibleByTwo(cont) and DivisibleByTwo(btcont):
                    self.board[self.size-1].append(Space(self.window,0,X,Y))
                elif not DivisibleByTwo(cont) and not DivisibleByTwo(btcont):
                    self.board[self.size-1].append(Space(self.window,1,X,Y))
                X += 28

            cwards = set()
            while change > 0:
                y = random.randint(0,self.size-1)
                x = random.randint(0,self.size-1)
                if (x,y) not in cwards:
                    cwards.add((x,y))
                    self.board[y][x].Empty()
                    change -=1
                

            #bord vew var
            self.chk.place_forget()
            self.chk.place(x=10,y=self.Hight-27)
        
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Binary_Square","PlayAgain",
                               f"failed to start new game",e],"Small Apps")

###################################################################
##################################################################

class Space:
    def __init__(self,window,binary,X,Y):
        self._Error = False
        #on space
        self.window = window
        self.anser = binary
        self.SHOWLST = ["  ",0,1]
        self.show = self.SHOWLST.index(self.anser)
        self.changeable = False
        #button
        self.space = Button(self.window,bg = "green",fg = "black",
                            font = ('timesnewroman 9 bold'),
                            text = f" {self.SHOWLST[self.show]} ",
                            command = self.Cange)
        self.space.place(x=X,y=Y)
        
    def Correct(self):
        try:
            if self.SHOWLST[self.show] == self.anser:
                self.space.configure(bg = "green")
                self.changeable = False
                return True
            elif self.show == 0:
                return None
        
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Space","Correct",
                               f"failed to check if corect",e],"Small Apps")
        return False

    def Empty(self):
        try:
            self.show = 0
            self.changeable = True
            self.space.configure(bg = "gray",
                              text = f" {self.SHOWLST[self.show]} ")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Space","Empty",
                               f"failed to set to empty",e],"Small Apps")

    def Cange(self):
        try:
            if self.changeable:
                self.show += 1
                if self.show > 2:
                    self.show = 0
                self.space.configure(text = f" {self.SHOWLST[self.show]} ")
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Space","Cange",
                               f"failed to change space",e],"Small Apps")

                    

##############################################################################
##############################################################################
if __name__ == "__main__":
    B = Binary_Square()

#self.PrintWhole(True,True,True,False)





















