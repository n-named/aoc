import re
from math import floor


with open('input.txt', 'r') as f:
    input_data = f.read()

input_data = [m.split("\n") for m in input_data.split("\n\n")]

tkns = 0
for m in input_data:
    d = {"A": {}, "B": {}, "P": {}}
    d["A"]["X"] = int(re.findall("X\+(\d{,2})", m[0])[0])
    d["A"]["Y"] = int(re.findall("Y\+(\d{,2})", m[0])[0])

    d["B"]["X"] = int(re.findall("X\+(\d{,2})", m[1])[0])
    d["B"]["Y"] = int(re.findall("Y\+(\d{,2})", m[1])[0])

    d["P"]["X"] = int(re.findall("X\=(\d{,5})", m[2])[0])
    d["P"]["Y"] = int(re.findall("Y\=(\d{,5})", m[2])[0])

    det = d["A"]["X"]*d["B"]["Y"] - d["B"]["X"]*d["A"]["Y"]
    A = (d["P"]["X"] * d["B"]["Y"] - d["B"]["X"] * d["P"]["Y"]) / det
    B = (d["A"]["X"] * d["P"]["Y"] - d["A"]["Y"] * d["P"]["X"]) / det
    
    if int(A)/ A != 1 or int(B)/ B != 1 or max(A,B) > 100:
        continue

    tkns = tkns + 3*A + B

print(int(tkns))
