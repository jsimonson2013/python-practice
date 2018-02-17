import sys

def selectionSort(array):
    sort = []
    used = []

    i = 0

    while i < len(array):
        best = None
        index = None

        for j in range(len(array)):
            if (j not in used):
                if (best == None or best > int(array[j])):
                    best = int(array[j])
                    index = j
        
        used.append(index)
        sort.append(best)

        i += 1

    return sort

def mergeSort(array):
    print("merge sort here")

if __name__ == "__main__":
    input = open(sys.argv[1], "r")

    arrayIn = []

    for line in input:
        arrayIn.append(line[:-1])
   
    print(arrayIn)
    print(selectionSort(arrayIn))
