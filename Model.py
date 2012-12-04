from View import View as Errors

class Model(object):


    def __init__(self):
        self.GameMap = {} # patern {Player:[(coordinate1),(coordinateN)]}




    def getPlayerMap(self,Player):
        Map = self.GameMap[Player]
        return Map

    def getMapping(self):
        Mapping = []
        for map in self.GameMap.values():
            Mapping += map

        return Mapping

    def getMappingNotLinear(self):
        Mapping = []
        for map in self.GameMap.values():
            Mapping.append(map)
        return Mapping


    def setCordinate(self,Player,TupleCoordinate):
        if Player in self.GameMap:
            self.GameMap[Player].append(TupleCoordinate)
        else :
            self.GameMap[Player]=[TupleCoordinate]









