import re


with open('input.txt', 'r') as f:
    input_data = f.read()

muls = re.findall("mul\((\d{1,3}),(\d{1,3})\)", input_data)

sum_muls = sum([int(f)*int(s) for f,s in muls])

print(sum_muls)
