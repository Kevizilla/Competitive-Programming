s = input().strip()
u = sum(1 for c in s if c.isupper())
l = len(s) - u
print(s.upper() if u > l else s.lower())