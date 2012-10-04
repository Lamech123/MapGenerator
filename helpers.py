import csv
import pickle

def creader(file):
    return csv.reader(open(file,"rb"))



object = Object()
filehandler = open(filename, 'w')
pickle.dump(object, filehandler)