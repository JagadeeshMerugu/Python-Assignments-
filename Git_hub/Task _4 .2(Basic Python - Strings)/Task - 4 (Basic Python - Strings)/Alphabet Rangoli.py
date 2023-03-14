import string

def print_rangoli(size):
    letters = string.ascii_lowercase[:size]
    width = 4 * size - 3
    
    for i in range(size-1,0,-1):
        line = '-'.join(letters[size - 1: i: -1] + letters[i: size])
        print(line.center(width, '-'))
    for i in range(size):
        line = '-'.join(letters[size - 1: i: -1] + letters[i: size])
        print(line.center(width, '-'))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
