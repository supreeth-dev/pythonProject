def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

#n = int(input())
n = 9
print("fibonacci sequeence")
fib =[]
for i in range(n):
    print(fibonacci(i))
    fib.append(fibonacci(i))

start = len(fib) -5
print(fib[start:])
file = "c:\\Users"
fp = open(file,'r')
