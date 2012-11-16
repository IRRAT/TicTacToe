class View(object):

    @staticmethod
    def tablePrint(n,m,Xcoordinates,Ocoordinates):
        print Xcoordinates,Ocoordinates
        table = [[" " for i in range(n)]for j in range(m)]
        for tupleCord in Xcoordinates:
            i,j = tupleCord
            print i,j
            table[i][j] = "X"
        for tupleCord in Ocoordinates:

            i,j = tupleCord
            print i,j
            table[i][j] = "O"


        for lines in table:
            print lines


    @staticmethod
    def GreatingMessage():
        CheckTibleSize = False
        print """
       (                                            )       
  *   ))\ )  (      *   )   (       (      *   ) ( /(       
` )  /(()/(  )\   ` )  /(   )\      )\   ` )  /( )\()) (    
 ( )(_))(_)|((_)   ( )(_)|(((_)(  (((_)   ( )(_)|(_)\  )\   
(_(_()|_)) )\___  (_(_()) )\ _ )\ )\___  (_(_())  ((_)((_)  
|_   _|_ _((/ __| |_   _| (_)_\(_|(/ __| |_   _| / _ \| __| 
  | |  | | | (__    | |    / _ \  | (__    | |  | (_) | _|  
  |_| |___| \___|   |_|   /_/ \_\  \___|   |_|   \___/|___| 
                                                            
                                                                                   
"""
        while CheckTibleSize == False:
            rows = int(raw_input(" \nplease input rows Number: "))
            lines = int(raw_input("please input lines Number: "))
            if rows < 3 or lines < 3 :
                print "\nERROR: number of rows and lines must be bigger than 2"
                continue
            CheckTibleSize = True
            
            
        
       
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
            if Winner == 1:
                Winner = "X"
            else :
                Winner = "O"
            
            
            
            print "Winnner is %s "%(Winner,)

    @staticmethod
    def ErrorMessageOut():
        print " Out of table "

    @staticmethod
    def ErrorMessageFree():
        print " Cell is no free "

    
