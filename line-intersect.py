import sys
import collections
import math

Line = collections.namedtuple('Line', ['endpt1', 'endpt2'])

# SSS law of Cosines to determine angle between lines pt1,p2 and pt1,p3
def angleMeasure(pt1, pt2, pt3):
    if (pt1 == pt2 or pt1 == pt3 or pt2 == pt3):
        return 0
    
    pt1 = pt1.split(",")
    pt2 = pt2.split(",")
    pt3 = pt3.split(",")

    pt1[0] = float(pt1[0])
    pt1[1] = float(pt1[1])
    pt2[0] = float(pt2[0])
    pt2[1] = float(pt2[1])
    pt3[0] = float(pt3[0])
    pt3[1] = float(pt3[1])

    side1 = math.sqrt(math.pow((pt1[0] - pt2[0]), 2) + math.pow((pt1[1] - pt2[1]), 2))
    side2 = math.sqrt(math.pow((pt1[0] - pt3[0]), 2) + math.pow((pt1[1] - pt3[1]), 2))
    side3 = math.sqrt(math.pow((pt3[0] - pt2[0]), 2) + math.pow((pt3[1] - pt2[1]), 2))

    if (2*side1*side2 == 0):
        return 0

    return math.degrees(math.acos((math.pow(side3, 2) - math.pow(side2, 2) - math.pow(side1, 2))/(-2.0*side1*side2)))

def isPointBetweenLine(point, line1, line2):
    if (angleMeasure(point, line1[1], line2[0]) + angleMeasure(point, line1[1], line2[1]) == angleMeasure(point, line2[0], line2[1])):
        return True
    else:
        return False

def doLinesIntersect(line1, line2):
    if (line1 == line2):
        return False
    if (isPointBetweenLine(line1[0], line1, line2) == True and isPointBetweenLine(line2[0], line2, line1)):
        return True
    else:
        return False

input = open(sys.argv[1], "r")

lines = []

# assumes input ends with newline
for line in input:
    lines.append(line[:-1])

for line1 in lines:
    endpts = line1.split(' ')
    line1 = Line(endpts[0], endpts[1])

    for line2 in lines:

        # format lines and check if intersect
        if (line1 != line2):
            endpts = line2.split(' ')
            line2 = Line(endpts[0], endpts[1])

            if (doLinesIntersect(line1, line2) == True):
                print 'Line {0} intersects line {1}'.format(line1, line2)
