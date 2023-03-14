# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input().strip())

for i in range(n):
    cc_number = input().strip()
    pattern = r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$'
    if re.match(pattern, cc_number) and not re.search(r'(\d)\1{3,}', cc_number.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")
