"""gamemap module to create and output a gamemap object"""


class Map:
    """gamemap class"""

    def __init__(self) -> None:
        self.map: list[list[int | str]] = []

    def make_map(self, size: int) -> list[list[int | str]]:
        """creates a map object"""
        grid: list[list[int | str]] = []
        for i in range(size):
            grid.append([])
            for _ in range(size):
                grid[i].append(0)
        return grid

    def print_map(self, grid: list[list[int | str]]) -> None:
        """print map object"""
        size = len(grid)
        print("    " + " ".join(str(i) for i in range(size)))
        border = "  " + "-" * (size * 2 + 2)
        print(border)

        for i in range(size):
            print(f"{i} | {' '.join(str(x) for x in grid[i])} |")

        print(border)

#Author: Luke Engelhardt
#Version: 1.0