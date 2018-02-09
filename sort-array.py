import sys

def selectionSort(array):
    print "selection sort here"

def mergeSort(array):
    print "merge sort here"

input = open(sys.argv[1], "r")

arrayIn = []

for line in input:
    arrayIn.append(line)
    
print arrayIn
