import math
import numpy
import json

with open("xTdata.json") as data:
    xTval = numpy.array(json.load(data))
    data.close

def xT(coordinate):
    if coordinate[0] == 120:
        coordinate[0] = 110
    if coordinate[1] == 110:
        coordinate[1] = 70
    return xTval[math.floor(coordinate[1]/10),
                 math.floor(coordinate[0]/10)]