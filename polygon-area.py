import sys

input = open(sys.argv[1], "r")

points = []

# assumes input ends with newline
for line in input:
    points.append(line[:-1])

