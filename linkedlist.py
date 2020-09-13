class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:

    def Single(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

if __name__ == '__main__':
    llist = linkedlist()

    llist.head = Node(1)
    s = Node(3)
    t = Node(2)

    llist.head.next = s
    s.next = t

    llist.AtBegining(6)
    llist.AtEnd(9)
    llist.Inbetween(llist.head.next.next, 50)
    llist.printList()