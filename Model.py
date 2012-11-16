from View import View as Errors

class Model(object):


    def __init__(self,lines,rows,win_case=3):

        self.rows = rows
        self.lines = lines   # 
        self.x_turns = []
        self.o_turns = [] #
        self.midleX = []
        self.midleO = []
        self.win_case = win_case #

    def getMidleX(self):
        return self.midleX

    def getMidleO(self):
        return self.midleO

    def addMidleX(self,value):
        self.midleX.append(value)


    def addMidleO(self,value):
        self.midleO.append(value)


    def get_win_case(self):
        return self.win_case-1

    def get_x_turn(self): # 
        return self.x_turns 

    def get_o_turn(self):
        return self.o_turns 
    
    def add_turnX(self,cordinates):
        self.check_valid(cordinates)
        self.x_turns.append(cordinates)


    def add_turnO(self,cordinates): # 
        self.check_valid(cordinates)
        self.o_turns.append(cordinates)


    def in_turnX(self, cordinate):
        return  cordinate in self.x_turns


    def in_turnO(self, cordinate): # 
        return  cordinate in self.o_turns


    def check_valid(self, cordinate): # 
        x,y = cordinate
        if x> self.rows or y > self.lines or x<0 or  y<0:
            Errors.ErrorMessageOut()
            return False

        if self.in_turnO(cordinate) or self.in_turnX(cordinate):
            Errors.ErrorMessageFree()
            return False
        return True

    
        




