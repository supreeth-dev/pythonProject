class Node:
    def __init__(self, data, nt):
        self.data = data
        self.nt = nt


class Linkedlist():
    def __init__(self):
        self.head = None

    def Insert_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def Insert_end(self, data):
        node = Node(data, None)
        temp = self.head
        while (temp.nt != None):
            temp = temp.nt
        temp.nt = node

    def Display(self):
        temp = self.head
        print("inside display")
        while (temp != None):
            print(temp.data)
            temp = temp.nt

    def Insert_middle(self, data, position):
        temp = self.head
        node = Node(data, None)
        i = 0
        while (i < position and temp != None):
            temp = temp.nt
            i = i + 1
        node.nt = temp.nt
        temp.nt = node

    def Delete(self, position):
        temp = self.head
        # node = Node(data,None)
        i = 0
        while (i < position and temp != None):
            prev = temp
            temp = temp.nt
            i = i + 1
        prev.nt = temp.nt


l1 = Linkedlist()
l1.Insert_begin(10)
l1.Insert_begin(20)
l1.Insert_begin(30)
l1.Insert_end(5)
l1.Insert_middle(25, 0)
l1.Delete(1)
l1.Display()

