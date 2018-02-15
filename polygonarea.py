import sys

def calculateArea(pts):
    area = 0.0
    for i in range(len(pts)):
        pti = pts[i].split(',')
        
        j = (i + 1) % len(pts)
        ptj = pts[j].split(',')

        area = area + float(pti[0]) * float(ptj[1]) - float(pti[1]) * float(ptj[0])

    return abs(area / 2.0)

if __name__ == "__main__":
    input = open(sys.argv[1], "r")

    points = []

    # assumes input ends with newline
    for line in input:
        points.append(line[:-1])

    print calculateArea(points)
