class map:
    def __init__(self):
        pass
        
    def makeMap(self, size):
        map = []
        for i in range(size):
            map.append([])
            for j in range(size):
                map[i].append(0)
        return map
    
    def printMap(self, map):
        for i in range(len(map)):
            print(map[i])
        return 0