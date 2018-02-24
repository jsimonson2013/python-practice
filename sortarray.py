import sys
import math

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

def mergeArrays(array1, array2):
    sort = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if int(array1[i]) < int(array2[j]):
            sort.append(array1[i])
            i += 1
        else:
            sort.append(array2[j])
            j += 1

    while i < len(array1):
        sort.append(array1[i])
        i += 1

    while j < len(array2):
        sort.append(array2[j])
        j += 1

    return sort


def mergeSort(array):
    if (len(array) < 2):
        return array
    
    midpt = int(len(array)/2)
    left = mergeSort(array[:midpt])
    right = mergeSort(array[midpt:])

    return mergeArrays(left, right)

if __name__ == "__main__":
    input = open(sys.argv[1], "r")

    arrayIn = []

    for line in input:
        arrayIn.append(line[:-1])
   
    print(arrayIn)
    print(mergeSort(arrayIn))
