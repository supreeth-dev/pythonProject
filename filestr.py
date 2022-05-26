import glob
import os
print(glob.glob('*'))
print(os.getcwd())

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class Linkedlist():
    def __init__(self):
        self.head = None
    def insert_start(self,data):

        node = Node(data,self.head)
        self.head = node
        #print(node.data)
    def print_data(self):
        itr = self.head
        count =0

        while itr:
            print(itr.data)
            itr = itr.next
    def delete_data(self,data):

        itr = self.head
        prev = itr
        while(itr):
            if(itr.data == data):
                print("found")
                #itr.next = itr.next.next
                if(itr == prev):
                    print("first")
                    print("--",itr.data)
                    itr = itr.next
                    prev = itr
                    print("--", prev.data)
                    #itr = itr.next
                    #print("--", itr.data)
                    continue
                prev.next = itr.next
            prev = itr
            itr = itr.next
    def delete(self,data):
        #node = self.head
        prev = curr = self.head
        while(curr):
            if(curr.data == data):
                print("Match ")
                if(curr == prev):
                    print("first",curr.data)
                    curr = curr.next
                    #prev = curr
                    self.head = curr
                    continue
                prev.next = curr.next
                print("after break")
            prev = curr
            curr = curr.next




l1 = Linkedlist()
l1.insert_start(10)
l1.insert_start(20)
l1.insert_start(30)
print("--------------")
l1.print_data()
l1.delete(30)
print("--------------")
l1.print_data()