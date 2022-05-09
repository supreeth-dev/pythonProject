
def smart_div(func):
    def inner(a,b):
        if(b>a):
            a,b = b,a
            print("inside innner function")
        return func(a,b)
    print("Inside wrapper function")
    return inner

def div(a,b):
    print(int(a/b))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 20
    b = 4
    div = smart_div(div)
    div(a,b)

