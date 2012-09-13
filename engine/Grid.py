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
