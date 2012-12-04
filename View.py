class View(object):
    NumberOfPlayers = 0
    Symbols = []




    @staticmethod
    def tablePrint(n,m,mapp):

        table = [[" " for i in range(n)]for j in range(m)]

        for i, ListCoord in enumerate(mapp):
            for pair in ListCoord:
                x,y = pair
                table[x][y] = View.Symbols[i]

        for lines in table:
            print lines


    @staticmethod
    def GreatingMessage():
        rows = int(raw_input(" please input rows Number "))
        lines = int(raw_input(" please input lines Number "))
        return rows,lines


    @staticmethod
    def InputMessage():
        print "plese make turn, input indexes: "

        x = int(raw_input(""))-1
        y = int(raw_input(""))-1
        return x,y

    @staticmethod
    def WinMessage(Winner = None):
        if Winner is not None:
            print "Winnner mesaage for %s "%(Winner,)

    @staticmethod
    def ErrorMessageOut():
        print " Out of table "

    @staticmethod
    def ErrorMessageFree():
        print " Cell is no free "

    @staticmethod
    def NamesOfPlayers():

        NumberOfPlayers = int(raw_input('Please enter number of players '))
        NamesOfPlayers = []
        for player in range(NumberOfPlayers):
            player_name = raw_input('Player%d please enter your name ' %player)
            NamesOfPlayers.append(player_name)

        return NamesOfPlayers,NumberOfPlayers
    @staticmethod
    def GenerateSymbols(NumberOfPlayers):

        Symbols = [chr(97+n) for n in range(NumberOfPlayers)]
        return Symbols





