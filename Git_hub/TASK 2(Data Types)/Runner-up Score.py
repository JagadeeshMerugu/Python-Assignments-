if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(set(arr)) # remove duplicates
    arr.sort(reverse=True) # sort in descending order
    if len(arr) < 2:
        print("No runner-up score")
    else:
        print(arr[1]) # print the second highest score
