class map:
    def __init__(self) -> None:
        self.map: list[list[int | str]] = []

    def makeMap(self, size: int) -> list[list[int | str]]:
        map: list[list[int | str]] = []
        for i in range(size):
            map.append([])
            for j in range(size):
                map[i].append(0)
        return map

    def printMap(self, map: list[list[int | str]]) -> None:
        size = len(map)
        print("    " + " ".join(str(i) for i in range(size)))
        border = "  " + "-" * (size * 2 + 2)
        print(border)

        for i in range(size):
            print(f"{i} | {' '.join(str(x) for x in map[i])} |")

        print(border)
