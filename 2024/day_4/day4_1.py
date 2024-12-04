import re
import numpy as np


with open('input.txt', 'r') as f:
    input_data_t = f.read()


ap = len(re.findall("(?=(XMAS|SAMX))", input_data_t))

input_data_m = [list(line) for line in input_data_t.split("\n")]
input_data_mt = list(zip(*input_data_m))

input_data_t = "\n".join(["".join(line) for line in input_data_mt])
ap = ap + len(re.findall("(?=(XMAS|SAMX))", input_data_t))

input_data_m = np.matrix(input_data_m)
for k in range(-len(input_data_m), len(input_data_m)):
    diag = "".join(np.diag(input_data_m, k))
    diag2 = "".join(np.diag(np.fliplr(input_data_m), k))
    ap = ap + len(re.findall("(?=(XMAS|SAMX))", diag)) + len(re.findall("(?=(XMAS|SAMX))", diag2))

print(ap)
