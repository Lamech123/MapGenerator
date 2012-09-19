# This class represents a data unit that will be entered into the tile blocks as dictated by their coordinates
class Data():

    # Constructor. Pass in the x, y, color and text of the Data
    def __init__(self, x, y, color, text, gridNumber):

        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.gridNumber = gridNumber