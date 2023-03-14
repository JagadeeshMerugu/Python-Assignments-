# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    s = ''

    for i in range(1, N, 2):

        s = s + (i * '.|.').center(M, "-") + "\n"

    s = s + 'WELCOME'.center(M, "-") + "\n"

    for i in range(N - 2, 0, -2):
        s = s + (i * '.|.').center(M, "-") + "\n"
        
    print(s)
