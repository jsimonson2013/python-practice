import sys
import node

input = open(sys.argv[1], "r")

head = node.Node("head\n", None)
curr = head

for line in input:
    curr.nextNode = node.Node(line, None)
    curr = curr.nextNode

curr = head
while curr.hasNext():
    print curr.data
    curr = curr.nextNode
print curr.data
