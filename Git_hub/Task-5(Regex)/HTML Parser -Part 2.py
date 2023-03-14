# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split('\n'))>1:
            print('>>> Multi-line Comment')
            for i in data.split('\n'):
                print(i)
        else:
            print('>>> Single-line Comment')
            print(data)
    def handle_data(self, data):
        for i in data.split('\n'):
            if len(i) != 0:
                print('>>> Data')
                print(i)

n = int(input())
org_string = ''''''
for i in range(0, n):
    s = input()
    org_string = org_string + f'{s}' + '\n'
parser = MyHTMLParser()
parser.feed(org_string)
