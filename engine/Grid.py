# This class represents a grid system created as a list.
class Grid():

    # Constructor. Pass in the width and height of the grid.
    def __init__(self, width, height, number):

        self.grid = []
        self.grid_width = width
        self.grid_height = height
        self.init_number = number

    def generate_grid(self):
        for row in range(self.grid_height):
            self.grid.append([])
            for column in range(self.grid_width):
                self.grid[row].append(0)

    def load_grid(self):
        self.grid = [["a21", "a20", "a19", "a18", "a17", "a16", "a15", "a14", "a13", "a12", "a11", "a10", "a9", "a8", "a7", "a6", "a5", "a4", "a3", "a2", "a1"],
                    ["b1", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ["c1", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]