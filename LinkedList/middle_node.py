
"""
Middle Node
You're given a Linked List with at least one node. Write a function that returns the middle node of the Linked List. If there are two middle nodes (i.e. an even length list), your function should return the second of these nodes.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / null if it's the tail of the list.

Sample Input
linkedList = 2 -> 7 -> 3 -> 5
Sample Output
3 -> 5 // The middle could be 7 or 3,
// we return the second middle node
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    if not linkedList.next:
        return linkedList
    
    slowNode = linkedList
    fastNode = linkedList
    
    while fastNode and fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode


