import sys
import polygonarea
import lineintersect
from lineintersect import Line

input = open(sys.argv[1], "r")

points = []

# assumes input ends with newline
for line in input:
    points.append(line[:-1])

print polygonarea.calculateArea(points)
print lineintersect.doLinesIntersect(Line(points[0], points[1]), Line(points[2], points[3]))
