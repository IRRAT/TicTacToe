
from Model import Model
from View import View

class Controller(object):

    def __init__(self):
        self.turn = 1  # 0- O, 1- X
        self.Model = None
        self.Winner = None



    def run(self):

        rows,lines = View.GreatingMessage()
        self.Model = Model(lines,rows)
        case = self.Model.get_win_case()
        View.tablePrint(rows,lines,[],[])

        Win = False

        while not Win:


            x,y = View.InputMessage()
            if not self.check_for_free((x,y)) or not self.Model.check_valid((x,y)):

                print "continue"
                continue
            turn = self.whose_turn()
            if turn == 0 :
                self.Model.add_turnO((x,y))
                    
            if turn == 1 :
                self.Model.add_turnX((x,y))


            Xcord = self.Model.get_x_turn()
            Ocord = self.Model.get_o_turn()
            View.tablePrint(rows,lines,Xcord,Ocord)
            Win = self.is_win((x,y))
        
            
        View.WinMessage(Winner=self.Winner)
        


    def is_win(self,last_cordinate):
        win_case = self.Model.get_win_case()
        if self.turn == 0: # 1-O, 0- X
            Xcords = self.Model.get_x_turn()
            if last_cordinate in self.Model.getMidleX():
                self.Winner = 1
                return True
            for cordinate in Xcords:
                dist = self.distanse(cordinate,last_cordinate)

                if dist ==  win_case or abs(dist-(2**0.5)*win_case)<0.0001:
                    print "dist acepted  "
                    middle_cell = self.calculate_middle_point(last_cordinate,cordinate)
                    print "---middle cell",middle_cell

                    
                    if middle_cell in Xcords:
                        self.Winner = 1
                        return True
                    else:
                        self.Model.addMidleX(middle_cell)


        if self.turn == 1: # 1-O, 0- X
            Ocords = self.Model.get_o_turn()
            if last_cordinate in self.Model.getMidleO():
                self.Winner = 0
                return True
            for cordinate in Ocords:
                dist = self.distanse(cordinate,last_cordinate)
                print "dist ",dist
                print "comparing: ",(2**0.5)*win_case,dist-(2**0.5)*win_case<0.0001

                if dist ==  win_case or dist-(2**0.5)*win_case<0.01:
                    middle_cell =  self.calculate_middle_point(last_cordinate,cordinate)
                    print middle_cell
                    if middle_cell in Ocords:
                        self.Winner = 0
                        return True
                    else:
                        self.Model.addMidleO(middle_cell)
                    
        self.Winner = 1
        return False
        return True


    def whose_turn(self):
        if self.turn == 0:
            self.turn = 1
            return 0
        if self.turn == 1:
            self.turn = 0
            return 1
        
    def check_for_free(self, cordinate):
        if self.Model.in_turnX(cordinate) or\
                    self.Model.in_turnX(cordinate):
            return False
        else:
            return True
                    
    def calculate_middle_point(self,head,tail):
        X,Y = head 
        x,y = tail
        if X<x:
            x,X = X,x
            y,Y = Y,y

        middle_points = None
        for i in range(x,X+1):
      
            for j in range(y,Y+1):
                if (x-i)*(Y-j)==(y-j)*(X-i) and (i,j)!=(x,y) and (i,j)!=(X,Y):
                    middle_points = (i,j)

        return middle_points

    def distanse(self,start_cord, end_cord):
        dist =  ((end_cord[0]-start_cord[0])**2+(end_cord[1]-start_cord[1])**2)**0.5
        return dist



Game  = Controller()
Game.run()

