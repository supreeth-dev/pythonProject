'''string = "abaabcccaaddde"
prev = None
count = 1
max_count = 1
rep_ch_list = []
for ch in string:
    #global count
    #print (count)
    if(ch == prev):
        #print(ch)
        count += 1
    else:
        if (count >= max_count):
            max_count = count
            rep_ch = prev
        count = 1
    ch.lower()

    prev = ch
print(rep_ch)
print(max_count)
print(string.count('ab'))'''


def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line =  "-".join(line)
    print(type(line))
    return line



if __name__ == '__main__':
    #line = input()
    line = "this is a string"
    result = split_and_join(line)
    print(result)


s = set("Hacker")
print( s.difference("Rank"))
print(s.union("Name"))


def count_substring(string, sub_string):

    j = 0
    count = 0
    for i in range(len(string)):
        print(i,j)
        if(string[i] == sub_string[j]):
            j =j+1
            print(string[i], " ", i, " ", j)
            if(len(sub_string) == j):
                count = count + 1
                print("count =", count)
                if(sub_string == sub_string[::-1]):
                    print("palindrome")
                    j=1
                else:
                    j=0
        else:
            j=0
        i = i+1
    print("occur",count)



if __name__ == '__main__':
    #string = input().strip()
    #sub_string = input().strip()
    string = "ABCDCDC"
    sub_string= "CD"
    count = count_substring(string, sub_string)
    print(count)