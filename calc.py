import math
import skilling
import items


def totem(totem, decoration):
    return (totem + decoration) * 0.2


def scale(in_value, inMin, inMax, outMin, outMax):
    return ((outMax-outMin) / (inMax-inMin))*(in_value - inMin) + outMin