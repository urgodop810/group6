import math
import numpy
import json

with open("xTdata.json") as data:
    xTval = numpy.array(json.load(data))
    data.close

def xT(coordinate):
    return xTval[math.floor(coordinate[0]/10),
                 math.floor(coordinate[1]/10)]
