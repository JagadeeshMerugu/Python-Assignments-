def count_substring(string, sub_string):
    count = 0
    while(True):
        if(sub_string in string):
            ind = string.index(sub_string)
            string = string[:ind] + string[ind+1:]
            count +=1
        else:
            break
    return count
if __name__ == '__main__':
