from html.parser import HTMLParser

class MyParser(HTMLParser):
    def print(self, action, tag, attrs=()):
        print(f"{action:5} : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")
        
    def handle_starttag(self, tag, attrs):
        self.print("Start", tag, attrs)

    def handle_endtag(self, tag):
        self.print("End", tag)

    def handle_startendtag(self, tag, attrs):
        self.print("Empty", tag, attrs)

parser = MyParser()
for _ in range(int(input())):
    parser.feed(input())
