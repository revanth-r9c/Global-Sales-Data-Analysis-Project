import random as rn
import numpy as np
class tictac:
    def __init__(self):
        self.board =  np.full([3,3],'-')
        self.state =  np.arange(1,10).reshape(3,3)
        self.chance = 0
        self.over = False
        self.x = np.array(['X','X','X'])
        self.o = np.array(['O','O','O'])
        self.statenames = [i for i in range(1,10)]
        self.option()
    
    def option(self):
        print(" ______________________________")
        print("|   Select the mode of game:   |")
        print("| 1:PLAY WITH ANOTHER PLAYER   |")
        print("| 2:PLAY WITH COMPUTER         |")
        print("|______________________________|")
        option = int(input("Enter your option: "))
        if option not in [1,2]:
            print("Enter a valid option...!!!")
            self.option()
        elif option == 1:
            self.pvsp()
        elif option == 2:
            self.pvsc()
       
                
    def pvsp(self):
        print("__________________________________")
        print("Cell representation")
        print(self.state)
        print("__________________________________")
        print("Player 1 --> 'O'.")
        print("Player 2 --> 'X'.")
        self.chance = 1
        while self.chance:
            if len(self.statenames) == 0:
                print("No more cells available...")
                print("Its a DRAW...!!!")
                return
            
            print("__________________________________")
            print("              Board               ")
            print(self.board)
            print("__________________________________")
            if self.chance == 1:
                print("Player 1's turn...")
            
                self.index = int(input("select the cell to add 'O': "))
                if self.index <= 0 or self.index > 9:
                    print("enter a valid location...")
                    continue
                if self.index in self.statenames:     
                    
                    self.i, self.j = np.where(state == self.index)
                    self.i, self.j = int(self.i) , int(self.j)
                    self.board[self.i][self.j] = "O"
                    print(self.state)
                    self.statenames.remove(self.index)
                    
                    self.check()
                    if self.over == True:
                        print(self.board)
                        print("***********************")
                        print("    Player 1 Won!!!    ")
                        print("      Game over...     ")
                        print("***********************")
                        self.chance = 0
                        continue
                        
                    else:
                        self.chance = 2
                        
                else :
                    print("Cell already taken...")
                    continue
                        
            elif self.chance==2 :
                print("Player 2's turn...")
            
                self.index = int(input("select the cell to add X :"))
                if self.index <= 0 or self.index > 9:
                    print("enter a valid location...")
                    continue
                    
                if self.index in self.statenames:
                    self.i, self.j = np.where(self.state == self.index)
                    self.i, self.j = int(self.i) , int(self.j)
                    self.board[self.i][self.j] = "X"
                    print(self.state)
                    self.statenames.remove(self.index)
                    
                    
                    self.check()
                    if self.over == True:
                        print(self.board)
                        print("***********************")
                        print("    Player 2 Won!!!    ")
                        print("      Game over...     ")
                        print("***********************")
                        self.chance = 0
                        continue
                        
                    else:
                        self.chance = 1
                        
                else:
                    print("Cell already taken...")
                    continue
                        
                        
    def check(self):
        self.d1 = []
        self.d2 = []
        
        if (self.i,self.j)  in [ (0,0) ,(0,2) ,(1,1) ,(2,1) ,(2,2)]:
            for a in range(3):
                self.d1.append(self.board[a][a])
                self.d2.append(self.board[2-a][2-a])
                
            self.m1 = np.array(self.d1)
            self.m2 = np.array(self.d2)
            if ((self.m1) == (self.x)).all() or ((self.m1) == (self.o)).all() or ((self.m2) == (self.x)).all() or ((self.m2) == (self.o)).all():
                self.over = True
                return
         
            if (self.board[:,self.j] == self.x).all()  or (self.board[:,self.j] == self.o).all()  or  (self.board[self.i,:] == self.x).all() or (self.board[self.i,:] == self.o).all():
                self.over = True
                return 
            else: 
                return 
        
        else:
            if((self.m1) == (self.x)).all() or ((self.m1) == (self.o)).all() or ((self.m2) == (self.x)).all() or ((self.m2) == (self.o)).all():
                self.over = True
                return
         
            if (self.board[:,self.j] == self.x).all()  or (self.board[:,self.j] == self.o).all()  or  (self.board[self.i,:] == self.x).all() or (self.board[self.i,:] == self.o).all():
                self.over = True
                return 
            else: 
                return 
            
            
    def pvsc(self):
        
        while self.chance:
            if len(self.statenames) == 0:
                print("No more cells available...")
                print("Its a DRAW...!!!")
                return
        print("__________________________________")
        print("Cell representation")
        print(self.state)
        print("__________________________________")
        print("You --> 'O'.")
        print("Computer --> 'X'.")
        self.chance = 1
        while self.chance:
            print("__________________________________")
            print("Board")
            print(self.board)
            print("__________________________________") 
            
            if self.chance == 1:
                print("Your turn...")
                
                self.index = int(input("select the cell to add 'O': "))
                if self.index <= 0 or self.index > 9:
                    print("enter a valid location...")
                    continue
                    
                if self.index in self.statenames:
                    self.i, self.j = np.where(self.state == self.index)
                    self.i, self.j = int(self.i) , int(self.j)
                    self.board[self.i][self.j] = "O"
                    print(self.state)
                    self.statenames.remove(self.index)
                    
                    
                    self.check()
                    if self.over == True:
                        print(self.board)
                        print("***********************")
                        print("       You Won!!!      ")
                        print("      Game over...     ")
                        print("***********************")
                        self.chance = 0
                        continue
                        
                    else:
                        self.chance = 2
                else:
                    print("Cell already taken...")
                    continue
                    
                        
            elif self.chance==2 :
                
                self.index = rn.choice(self.statenames)
                
                    
                print("THE computer selected : ", self.index)
                self.i, self.j = np.where(self.state == self.index)
                self.i, self.j = int(self.i) , int(self.j)
                self.board[self.i][self.j] = "X"
                print(self.state)
                self.statenames.remove(self.index)
                self.check()
                if self.over == True:
                    print(self.board)
                    print("***************************")
                    print("       Computer Won!!!     ")
                    print("        Game over...       ")
                    print("***************************")
                    self.chance = 0
                    continue
                else:
                    self.chance = 1            
        
game = tictac()