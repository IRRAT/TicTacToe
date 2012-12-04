
from Model import Model
from View import View


class Controller(object):


    matches  =  3


    class Player(object):
        def __init__(self,Name):
            self.Name = Name
            self.Winner = False
              # {(x1,y1):PlayerName}

        def getName(self):
            return self.Name

        def isWinner(self):
            return self.Winner


    class Turner(object):
        def __init__(self,PlayersList):
            self.Players = PlayersList
            self.CurentState = 0

        def getNext(self):
            Player = self.Players[self.CurentState]
            if self.CurentState==len(self.Players)-1:
                self.CurentState = 0
            else :
                self.CurentState = self.CurentState+1

            return Player

    def __init__(self):
        self.Players =[]
        self.Model  =  Model()
        self.intermediatePoints = {}
#        self.Turner  = Controller.Turner()

    def run(self):

        self.rows,self.lines = View.GreatingMessage()

        self.NamesOfPlayers,View.NumberOfPlayers = View.NamesOfPlayers() # intial Players from View

        for name in self.NamesOfPlayers:
            player = Controller.Player(name)
            self.Players.append(player)







        self.Turner  = Controller.Turner(self.Players)

        View.Symbols = View.GenerateSymbols(View.NumberOfPlayers)
        View.tablePrint(self.rows,self.lines,[])

        Win = False

        while not Win:
            CurentPlayer = self.Turner.getNext()
            print "Hello ", CurentPlayer.getName()
            x,y = View.InputMessage()

            if not self.ValidCoordinate((x,y)):
                print "continue"
                self.Turner.CurentState = self.Turner.CurentState - 1
                continue
            self.Model.setCordinate(CurentPlayer,(x,y))
            mapp = self.Model.getMappingNotLinear()
            View.tablePrint(self.lines,self.rows,mapp)

            Win = self.is_win(CurentPlayer,(x,y))
        
            pass
        View.WinMessage(Winner=self.Winner)



    def is_win(self,Player,last_cordinate):
        CordList = self.Model.getPlayerMap(Player)
        if Player in self.intermediatePoints and last_cordinate in self.intermediatePoints[Player]:

            self.Winner = Player.getName()
            return True

        for cordinate in CordList:
            dist = self.distanse(cordinate,last_cordinate)

            if dist ==  Controller.matches-1 or abs(dist-(2**0.5)*(Controller.matches-1))<0.0001:
                print "dist acepted  "
                innerPoint =   self.solver(last_cordinate,cordinate)
                print "---sub cell",innerPoint

                    
                if innerPoint in CordList:
                    self.Winner = Player.getName()
                    return True
                else:
                    if Player in self.intermediatePoints:
                        self.intermediatePoints[Player].append(innerPoint)
                    else :
                        self.intermediatePoints[Player] = [innerPoint]

        self.UpdatingInerPoint(last_cordinate)
        return False



        
    def ValidCoordinate(self, cordinate):
        x,y = cordinate
        if x> self.rows or y > self.lines or x<0 or  y<0:
            View.ErrorMessageOut()
            return False
        if cordinate in self.Model.getMapping():
            View.ErrorMessageFree()
            return False
        return True


    def solver(self,head,tail):
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


    def UpdatingInerPoint(self,CoordTuple):
        for Player in self.intermediatePoints:
            for pair in self.intermediatePoints[Player]:
                if CoordTuple==pair:
                    self.intermediatePoints[Player].remove(pair)



Game  = Controller()
Game.run()

