#program:       Binary_Square
#purpose:       makes the board
#progamer:      Themadhood Pequot 7/26/2022

_FILE = "Binary_Square"
_VERSION = "0.0.2"

import random
random.seed()
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import Error
    
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
    def __init__(self,error = False):
        self._Error = error
        #creates the window
        self.window = Tk()
        self.window.iconbitmap(default = FP +"/Binery_Game_icon.ico")
        self.window.title("Binery Square")#title of widow
        self.window.config(bg='black')#collor

        #bord vew var
        self.chk = Button(self.window,bg = "gray",fg = "black",
                   font = ('timesnewroman 9 bold'),
                   text = "Check",
               command=self.Check)

        self.PlayAgain()
        

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

            self.Updatelbls()

            if fail:
                playAgain = messagebox.askyesno('You Loose',
                                                 'Do you want to play again?')
            elif not fail and end:
                playAgain = messagebox.askyesno('You Win',
                                                 'Do you want to play again?')
            if playAgain and end:
                for i in range(0,self.size):
                    for j in range(0,self.size):
                        self.board[i][j].space.grid_forget()
                for v in self.lbls['V']:
                    v.grid_forget()
                for h in self.lbls['H']:
                    h.grid_forget()
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
            
            self.Hight = (28 * self.size) + 90
            self.WITH = (26 * self.size) + 99
            #size (X)x(Y) location  +(X)+(Y)
            self.window.geometry(f"{self.WITH}x{self.Hight}")
            
            binery = [0,1]
            #creates the board
            self.board = []
            Y = 0 + 3
            for i in range(0,self.size-1):
                self.board.append([])
                for j in range(0,self.size-1):
                    space = random.randint(0,1)
                    self.board[i].append(Space(self.window,binery[space],i,j))

            self.lbls = {'V':[],
                         'H':[]}
            #virtical Check
            for i in range(0,self.size-1):
                cont = zeros = ones = 0
                for j in range(0,self.size-1):
                    cont += self.board[i][j].anser
                    num = self.board[i][j].GetNum()
                    if num == 1:
                        ones += 1
                    elif num == 0:
                        zeros += 1
                    
                if DivisibleByTwo(cont):
                    self.board[i].append(Space(self.window,0,i,self.size-1,"orange"))
                    zeros += 1
                else:
                    self.board[i].append(Space(self.window,1,i,self.size-1,"orange"))
                    ones += 1
                
                self.lbls["V"].append(Label(self.window,bg="black",fg="grey",
                                            text = f"1's:{ones}\t0's:{zeros}",
                                            font = (f'timesnewroman 9 bold')))
                self.lbls["V"][i].grid(row=i,column=self.size,padx=1,pady=1)

            #horizontal Check
            btcont = 0
            self.board.append([])
            for i in range(0,self.size):
                cont = zeros = ones = 0
                for j in range(0,self.size-1):
                    cont += self.board[j][i].anser
                    num = self.board[i][j].GetNum()
                    if num == 1:
                        ones += 1
                    elif num == 0:
                        zeros += 1

                if DivisibleByTwo(cont) and i < self.size-1:
                    self.board[self.size-1].append(Space(self.window,0,self.size-1,i,"orange"))
                    zeros += 1
                elif not DivisibleByTwo(cont) and i < self.size-1:
                    self.board[self.size-1].append(Space(self.window,1,self.size-1,i,"orange"))
                    ones += 1
                    btcont +=1
                elif DivisibleByTwo(cont) and DivisibleByTwo(btcont):
                    self.board[self.size-1].append(Space(self.window,0,self.size-1,i,"orange"))
                    zeros += 1
                elif not DivisibleByTwo(cont) and not DivisibleByTwo(btcont):
                    self.board[self.size-1].append(Space(self.window,1,self.size-1,i,"orange"))
                    ones += 1

                self.lbls["H"].append(Label(self.window,bg="black",fg="grey",
                                            text = f"1's\n{ones}\n\n0's\n{zeros}",
                                            font = (f'timesnewroman 9 bold')))
                self.lbls["H"][i].grid(row=self.size,column=i,padx=1,pady=1)

            cont = zeros = ones = 0
            for j in range(0,self.size):
                num = self.board[j][self.size-1].GetNum()
                if num == 1:
                    ones += 1
                elif num == 0:
                    zeros += 1
                
            self.lbls["V"].append(Label(self.window,bg="black",fg="grey",
                                            text = f"1's:{ones}\t0's:{zeros}",
                                            font = (f'timesnewroman 9 bold')))
            self.lbls["V"][self.size-1].grid(row=self.size-1,column=self.size,padx=1,pady=1)

            cwards = set()
            while change > 0:
                y = random.randint(0,self.size-1)
                x = random.randint(0,self.size-1)
                if (x,y) not in cwards:
                    cwards.add((x,y))
                    self.board[y][x].Empty()
                    change -=1

            self.Updatelbls()
                

            #bord vew var
            try:
                self.chk.grid_forget()
            except:
                pass
            self.chk.grid(row=self.size,column=self.size,padx=1,pady=1,
                          columnspan=2,sticky="nesw")
        
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Binary_Square","PlayAgain",
                               f"failed to start new game",e],"Small Apps")

    def Updatelbls(self):
        try:
            #virtical Check
            for i in range(0,self.size):
                zeros = ones = 0
                for j in range(0,self.size):
                    
                    num = self.board[i][j].GetNum()
                    if num == 1:
                        ones += 1
                    elif num == 0:
                        zeros += 1
                self.lbls["V"][i].config(text = f"1's:{ones}\t0's:{zeros}")

                
            #horizontal Check
            for i in range(0,self.size):
                zeros = ones = 0
                for j in range(0,self.size):
                    num = self.board[j][i].GetNum()
                    if num == 1:
                        ones += 1
                    elif num == 0:
                        zeros += 1
                self.lbls["H"][i].config(text = f"1's\n{ones}\n\n0's\n{zeros}")

                
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Binary_Square","PlayAgain",
                               f"failed to start new game",e],"Small Apps")

###################################################################
##################################################################

class Space:
    def __init__(self,window,binary,X,Y,edge="green"):
        self._Error = False
        self.bg = edge
        #on space
        self.window = window
        self.anser = binary
        self.SHOWLST = ["  ",0,1]
        self.show = self.SHOWLST.index(self.anser)
        self.changeable = False
        #button
        self.space = Button(self.window,bg = self.bg,fg = "black",
                            font = ('timesnewroman 9 bold'),
                            text = f" {self.SHOWLST[self.show]} ",
                            command = self.Cange)
        
        self.space.grid(row=X,column=Y,padx=1,pady=1)

    def GetNum(self):
        return self.SHOWLST[self.show]
        
    def Correct(self):
        try:
            if self.SHOWLST[self.show] == self.anser:
                self.space.configure(bg = self.bg)
                self.changeable = False
                return True
            elif self.show == 0:
                return None
        
        except Exception as e:
            if self._Error:
                raise
            Error.UploadError([_FILE,_VERSION,"Space","Correct",
                               f"failed to check if corect",e],"Small Apps")
        self.space.configure(bg = "red")
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
    B = Binary_Square(True)

#self.PrintWhole(True,True,True,False)

#columnspan, -in, -ipadx, -ipady, -rowspan, or -sticky



















