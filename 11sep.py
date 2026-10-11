# py List Comprehension
b = [10, 80, 95, 70]
n=[]
for x in b:
    if x >=90:
        c="A"
    elif x > 75:
        c="B"
    else:
        c="C"
    n.append((x, c))
print(n)