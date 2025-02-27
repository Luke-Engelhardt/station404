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
        size = len(map)
        print("    " + " ".join(str(i) for i in range(size)))
        border = "  " + "-" * (size * 2 + 2) 
        print(border)
        
        for i in range(size):
            print(f"{i} | {' '.join(str(x) for x in map[i])} |")
            
        print(border)
    
    