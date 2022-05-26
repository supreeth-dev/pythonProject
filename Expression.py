from collections import deque

class stack:
    def __init__(self):
        stack.container = deque()

    def push(self,data):
        stack.container.append(data)

    def pop(self):
        return stack.container.pop()

    def top(self):
        if(self.is_empty()):
            return False
        else:
            return stack.container[self.size()-1]

    def size(self):
        return len(stack.container)

    def is_empty(self):
        return len(stack.container) == 0

    def is_balanced(self,string):
        for ch in string:
            print(ch)
            if(ch == '(' or ch == '{' or ch == '['):
                self.push(ch)
            elif(ch == ')' and self.top() == '('):
                self.pop()
            elif (ch == ']' and self.top() == '['):
                self.pop()
            elif (ch == '}' and self.top() == '{'):
                self.pop()
        print(self.top())

        if(self.is_empty()):
            print("Valid Expression")
        else:
            print("Not a valid Expression")

s1 = stack()


print(s1.top())
#print(s1.pop())

string = "({a+b})(]"
s1.is_balanced(string)