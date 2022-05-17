def count_substring(string, sub_string):
    j = 0
    count = 0
    for i in range(len(string)):
        if (string[i] == sub_string[j]):
            j = j + 1

            if (len(sub_string) == j):
                count = count + 1

                if (sub_string == sub_string[::-1]):

                    j = 1
                else:
                    j = 0
        else:
            j = 0
        i = i + 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)