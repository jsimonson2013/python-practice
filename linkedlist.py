import sys
import node

def toString(head):
    curr = head
    while curr.hasNext():
        print(curr.data)
        curr = curr.nextNode

    print(curr.data)

if __name__ == "__main__":
    input = open(sys.argv[1], "r")

    head = node.Node("head\n", None)
    curr = head

    for line in input:
        curr.nextNode = node.Node(line, None)
        curr = curr.nextNode
    
    toString(head)
