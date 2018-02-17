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

def recursivelyMergeAndSort(array1, array2):

    if (len(array1) < 2 or len(array2) < 2):
        if int(array1[0]) < int(array2[0]):
            return array1 + array2
        else:
            return array2 + array1
    else:
        midptArray1 = int(len(array1)/2)
        midptArray2 = int(len(array2)/2)
        return recursivelyMergeAndSort(array1[:midptArray1], array1[midptArray1:]) + recursivelyMergeAndSort(array2[midptArray2:], array2[:midptArray2])



def mergeSort(array):
    sort = []
    if (len(array) < 2):
        return array

    midpt = int(len(array)/2)
    return recursivelyMergeAndSort(array[:midpt], array[midpt:])

if __name__ == "__main__":
    input = open(sys.argv[1], "r")

    arrayIn = []

    for line in input:
        arrayIn.append(line[:-1])
   
    print(arrayIn)
    print(mergeSort(arrayIn))
