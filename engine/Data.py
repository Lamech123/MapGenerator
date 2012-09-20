# This class represents a data unit that will be entered into the tile blocks as dictated by their coordinates
class Data():

    # Constructor. Pass in the x, y, color and text of the Data
    def __init__(self, x, y, color, text, gridNumber):

        self.x = x
        self.y = y
        self.color = color
        self.text = text

        #Create a data point

#data1 = Data(1,5,GREEN, "Titanic", "a1")
#self.datum.append(data1)
#data2 = Data(2,7, RED, "Coal Strike", "a2")
#self.datum.append(data2)
#
#for data in self.datum:
#    grid.grid[data.x][data.y] = data.gridNumber