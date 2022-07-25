a, b = input().split()
a = int(a)
b = int(b)
#c = (a if (a>=b) else b)
if a>=b:
    c = a
else:
    c = b
print(int(c))
