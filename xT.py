import math
import numpy

xTval = numpy.array([
                    [
                       0.00638303,
                       0.00779616,
                       0.00844854,
                       0.00977659,
                       0.01126267,
                       0.01248344,
                       0.01473596,
                       0.0174506,
                       0.02122129,
                       0.02756312,
                       0.03485072,
                       0.0379259
                    ],
                    [
                       0.00750072,
                       0.00878589,
                       0.00942382,
                       0.0105949,
                       0.01214719,
                       0.0138454,
                       0.01611813,
                       0.01870347,
                       0.02401521,
                       0.02953272,
                       0.04066992,
                       0.04647721
                    ],
                    [
                       0.0088799,
                       0.00977745,
                       0.01001304,
                       0.01110462,
                       0.01269174,
                       0.01429128,
                       0.01685596,
                       0.01935132,
                       0.0241224,
                       0.02855202,
                       0.05491138,
                       0.06442595
                    ],
                    [
                       0.00941056,
                       0.01082722,
                       0.01016549,
                       0.01132376,
                       0.01262646,
                       0.01484598,
                       0.01689528,
                       0.0199707,
                       0.02385149,
                       0.03511326,
                       0.10805102,
                       0.25745362
                    ],
                    [
                       0.00941056,
                       0.01082722,
                       0.01016549,
                       0.01132376,
                       0.01262646,
                       0.01484598,
                       0.01689528,
                       0.0199707,
                       0.02385149,
                       0.03511326,
                       0.10805102,
                       0.25745362
                    ],
                    [
                       0.0088799,
                       0.00977745,
                       0.01001304,
                       0.01110462,
                       0.01269174,
                       0.01429128,
                       0.01685596,
                       0.01935132,
                       0.0241224,
                       0.02855202,
                       0.05491138,
                       0.06442595
                    ],
                    [
                       0.00750072,
                       0.00878589,
                       0.00942382,
                       0.0105949,
                       0.01214719,
                       0.0138454,
                       0.01611813,
                       0.01870347,
                       0.02401521,
                       0.02953272,
                       0.04066992,
                       0.04647721
                    ],
                    [
                       0.00638303,
                       0.00779616,
                       0.00844854,
                       0.00977659,
                       0.01126267,
                       0.01248344,
                       0.01473596,
                       0.0174506,
                       0.02122129,
                       0.02756312,
                       0.03485072,
                       0.0379259
                    ]
                                    ])

def xT(c):
    Cor = [math.floor(c[0]/10),math.floor(c[1]/10)]
    return xTval[Cor[0],Cor[1]]
