import re

repl = lambda x: x.group().replace('&&', 'and').replace('||', 'or')
for _ in range(int(input())):
    print(re.sub(r'(?<= )\&\& |(?<= )\|\| ', repl, input()))
