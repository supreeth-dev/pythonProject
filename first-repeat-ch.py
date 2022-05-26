string = "aaabbcddeef"
dict = {}
for ch in string:
    #print(ch)
    if(ch in dict.keys() ):
        dict[ch] = dict[ch] +1
    else:
        dict[ch] = 1
#print(dict)
for ch in string:
    if(dict[ch] == 1):
        print ("First non repested chearcter is ",ch)
        break

for ch in set(string):
    #print (ch)
    dict[ch] = string.count(ch)
print(dict)