import sys
import collections

Line = collections.namedtuple('Line', ['endpt1', 'endpt2'])

def areParallel(line1, line2):
    return False

def directionFromPointToPoint(pt1, pt2):
    # how to do this?
    return -1

def isPointBetweenLine(pt, line):
    if (directionFromPointToPoint(pt, line[0]) != directionFromPointToPoint(pt, line[1] > 0)):
        return True

def doLinesIntersect(line1, line2):
    if (areParallel(line1, line2) == True):
        return False
    if (isPointBetweenLine(line1[0], line2) == True and isPointBetweenLine(line2[0], line1)):
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
