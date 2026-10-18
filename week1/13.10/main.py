import csv
x= '"Class",I0,"PA500","HFS","DA","Area","A.DA","Max.IP","DR","P"'

y=csv.reader([x])
v=next(y)    
print(v)



# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# FILE_INPUT = BASE_DIR / data / data.csv

# print(FILE_INPUT)