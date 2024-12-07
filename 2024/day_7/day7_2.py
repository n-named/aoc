import re


with open('input.txt', 'r') as f:
    input_data = f.read()

tests = [int(num) for num in re.findall("(\d*):", input_data)]
data = [[int(num) for num in re.findall(" \d*", line)] for line in input_data.split("\n")]

total = 0

for eq in range(len(data)):
    for t in range(3**(len(data[eq]) - 1)):
        ops = ""
        while t > 0:
            ops = str(t % 3) + ops
            t = t // 3
            
        if len(ops) < len(data[eq]) - 1 or ops == '':
            ops = "0"*(len(data[eq])-1 - len(ops)) + ops
            
        s = data[eq][0]
        for i in range(len(ops)):
            if ops[i] == "0":
                s = s + data[eq][i+1]
            elif ops[i] == "1":
                s = s * data[eq][i+1]
            elif ops[i] == "2":
                s = int(str(s) + str(data[eq][i+1]))
                
        if s == tests[eq]:
            total = total + tests[eq]
            break

print(total)
