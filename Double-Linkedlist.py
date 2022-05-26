class Node():
    def __init__(self,data,nxt,prv):
        self.data = data
        self.prv = prv
        self.nxt = nxt

class Double_linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert_begin(self, data):

        node = Node(data, self.head, self.tail)
        if(self.head == None):
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head.prv = node
            self.head = node
    def Insert_end(self, data):
        print("Insert end function ")
        node = Node(data, self.head, self.tail)
        if(self.head == None):
            print("first node ")
            self.head = node
            self.tail = node
            print("outside if ",self.tail.data)
        else:
            node.prv = self.tail
            self.tail.nxt = node
            self.tail = node

    def Display(self):
        temp = self.head
        while(temp != self.tail):
            print(temp.data)
            temp = temp.nxt
        print(temp.data)
l1 = Double_linkedlist()
l1.Insert_begin(30)
l1.Insert_begin(40)
l1.Insert_begin(50)
l1.Insert_end(10)

l1.Display()