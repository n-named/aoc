import re


with open('input.txt', 'r') as f:
    input_data = f.read()

tests = [int(num) for num in re.findall("(\d*):", input_data)]
data = [[int(num) for num in re.findall(" \d*", line)] for line in input_data.split("\n")]

total = 0

for eq in range(len(data)):
    for b in range(2**(len(data[eq]) - 1)):
        ops = bin(b)[2:]
        ops = "0"*(len(data[eq])-1 - len(ops)) + ops
        
        s = data[eq][0]
        for i in range(len(ops)):
            if ops[i] == "0":
                s = s + data[eq][i+1]
            elif ops[i] == "1":
                s = s * data[eq][i+1]
                
        if s == tests[eq]:
            total = total + tests[eq]
            break

print(total)
