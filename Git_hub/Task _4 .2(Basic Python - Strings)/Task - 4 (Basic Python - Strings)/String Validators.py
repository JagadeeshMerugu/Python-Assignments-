if __name__ == '__main__':
    s = input()
    
    
    b=[False,False,False,False,False]
    for i in s:
        if i.isalnum():
            b[0]=True
        if i.isalpha():
            b[1]=True
        if i.isdigit():
            b[2]=True
        if i.islower():
            b[3]=True
        if i.isupper():
            b[4]=True
    for i in b:
        print(i)
