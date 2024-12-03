import re


with open('input.txt', 'r') as f:
    input_data = f.read()

muls = re.findall("mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", input_data)

sum_muls = 0

do = 1
for el in muls:
    if "don't()" in el:
        do = 0
    elif "do()" in el:
        do = 1
    elif do:
        sum_muls = sum_muls + int(el[0])*int(el[1])

print(sum_muls)
