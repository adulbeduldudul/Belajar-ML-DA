# py List Comprehension

# 2
x=[10, 80, 95, 70]

a = [
    "a" if x > 90 else "b" if x > 75 else "c"
    for x in x
]
print(list(zip(x, a)))



#  1
# b = [10, 80, 95, 70]
# n=[]
# for x in b:
#     if x >=90:
#         c="A"
#     elif x > 75:
#         c="B"
#     else:
#         c="C"
#     n.append((x, c))
# print(n)