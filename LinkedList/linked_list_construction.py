"""
Linked List Construction
Write a DoublyLinkedList class that has a head and a tail, both of which point to either a linked list Node or None / null. The class should support:

Setting the head and tail of the linked list.
Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1).
Removing given nodes and removing nodes with given values.
Searching for nodes with given values.
Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition, and remove methods all take in actual Nodes as input parameters—not integers (except for insertAtPosition, which also takes in an integer representing the position); this means that you don't need to create any new Nodes in these methods. The input nodes can be either stand-alone nodes or nodes that are already in the linked list. If they're nodes that are already in the linked list, the methods will effectively be moving the nodes within the linked list. You won't be told if the input nodes are already in the linked list, so your code will have to defensively handle this scenario.

If you're doing this problem in an untyped language like Python or JavaScript, you may want to look at the various function signatures in a typed language like Java or TypeScript to get a better idea of what each input parameter is.

Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node or None / null.

Sample Usage
// Assume the following linked list has already been created:
1 <-> 2 <-> 3 <-> 4 <-> 5
// Assume that we also have the following stand-alone nodes:
3, 3, 6
setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6
insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 in position 1
removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
containsNodeWithValue(5): true
""" 

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        node = Node(node)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    def setTail(self, node):
        current = self.head
        while current and current.next:
            current = current.next
        
        node= Node(node)
        node.prev = current
        current.next = node
        

    def insertBefore(self, node, nodeToInsert):
        current = self.head
        new_node = Node(nodeToInsert)
        while current and current.next:
            if current.value == node:
                new_node.next = current
                
                if current == self.head:
                    self.head = new_node
                else:
                    new_node.prev = current.prev
                current.prev = node
                return
            current = current.next
            

    def insertAfter(self, node, nodeToInsert):
        current = self.head
        new_node = Node(nodeToInsert)
        while current and current.next:
            if current.value == node:
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                return
            current = current.next

    def insertAtPosition(self, position, nodeToInsert):
        current = self.head
        for i in range(1, 1):
            current = current.next
        
        node = Node(nodeToInsert)
        if current == self.head:
            self.head = node
        else:
            current.prev.next = node
        node.prev = current.prev
        node.next = current

    def removeNodesWithValue(self, value):
        # Write your code here.
        current = self.head
        while current and current.next:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                else:
                    current.prev.next = current.next

                if not current.next:
                    current.next.prev = current.prev
            current = current.next

    def remove(self, node):
        # Write your code here.
        current = self.head
        while current and current.next:
            if current.value == node:
                if current == self.head:
                    self.head = current.next
                    continue
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next


    def containsNodeWithValue(self, value):
        # Write your code here.
        current = self.head
        while current and current.next:
            if current.value == value:
                return True
            current = current.next
            
        return False
