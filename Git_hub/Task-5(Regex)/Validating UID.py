import re
for _ in range(int(input())):
    s = input()
    match = bool(re.match(r"^[a-zA-Z0-9]{10}$", s)) and not bool(re.findall(r'(.)(?=.*\1)', s)) and bool(re.search(r'\d.*\d.*\d', s)) and bool(re.search(r'[A-Z].*[A-Z]', s))
    print('Valid' if match else 'Invalid')
