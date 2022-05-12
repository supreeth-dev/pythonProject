class Node:
    def __init__(self,data,next ):
        self.data = data
        self.next = next

class Linkedlist():
    def __init__(self):
        self.head = None

    def insert(self,data ):
        node = Node(data,self.head)
        self.head =node
    def display(self):
        itr = self.head
        while(itr):
            print(itr.data)
            itr = itr.next
    def reverse(self):
        prev = None
        #next = None
        next = curr = self.head
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def delete(self,data):
        #node = self.head
        prev = curr = self.head
        while(curr):
            if(curr.data == data):
                print("Match ")
                if(curr == prev):
                    print("first")
                    curr = curr.next
                    prev = curr
                    curr = curr.next
                    continue
                prev.next = curr.next
                print("after break")
            prev = curr
            curr = curr.next



l1 = Linkedlist()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.display()
print("-------")
l1.reverse()
print("-------")
l1.display()
print("-------")
l1.delete(10)
print("-------")
l1.display()
