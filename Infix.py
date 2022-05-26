from queue import Queue
class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if(self == None):
            return BST(data)
        if(self.data == data):
            return

        if(data < self.data):
            if(self.left):
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if(self.right):
                self.right.insert(data)
            else:

                self.right = BST(data)

    def inoder(self):
        ele =[]
        #parse left tree
        if self.left:
            ele += self.left.inoder()
            #print("left=",ele)
        #visit base node
        ele.append(self.data)
        #print("data= ",self.data)

        #parse right tree
        if self.right:
            ele += self.right.inoder()
            #print("right=", ele)

        return ele

    def search_tree(self,data):
        #print(data)
        #print(self.data)
        if(self.data == data):
            print("match--")
            return True
        if(data < self.data):
            if(self.left):
                self.left.search_tree(data)
            else:
                return False
        if(data > self.data):
            if(self.right):
                self.right.search_tree(data)
            else:
                return False

def build_tree(ele):
    print(ele[0])
    root = BST(ele[0])

    for i in range(1,len(ele)):
        root.insert(ele[i])
    return root




if __name__ == '__main__':
    numbers = [17,20,4,1,20,23,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.inoder())
    val = numbers_tree.search_tree(20)z
    print(val)

