#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from engine.Data import Data
import csv

# This class represents a record that contains all of the data points
class Record(object):

    # Constructor. Pass in the x, y, color and text of the Data
    def __init__(self, csv_file):

        self.csv_file = csv_file
        self.record = []

        for row in self.csv_file:
            data = Data(row[0], row[1], row[2], row[3])
            self.record.append(data)

    def __str__(self):

        res = []
        for data in self.record:
            res.append(str(data))
        return "\n".join(res)

