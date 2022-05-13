def wrapper(expr):
    def upper(func):
        def inner():
            str1 = func()

            return str1.upper()+ expr.upper()
        return inner
    return upper



'''def wrapper(expr):
    def upper(func):
        def inner():
            str1 = func()
            return str1.upper() + expr.upper() 
        return inner
    return upper'''
@wrapper(expr)
def ordinary():
    return "Good Morning"
print(ordinary())



