import re
from math import floor


with open('input.txt', 'r') as f:
    input_data = f.read().split("\n")

h = 103
w = 101

for k in range(1, 10000):
    t_map = [[" " for col in range(w)] for row in range(h)]

    for robot in input_data:
        reg = re.findall("=(-?\d{,3}),(-?\d{,3})", robot)

        p = [int(reg[0][0]), int(reg[0][1])]
        v = [int(reg[1][0]), int(reg[1][1])]

        kpv = [k*v[0], k*v[1]]

        crd = [p[0] + kpv[0], p[1] + kpv[1]]
        crd[0] = crd[0]%w
        crd[1] = crd[1]%h

        t_map[crd[1]][crd[0]] = "#"
    
    t_map = "\n".join(["".join(l) for l in t_map])

    tr_base = t_map.find(" ### ")
    if tr_base == -1:
        continue

    try:
        if t_map[tr_base-101 + 1] == t_map[tr_base+101 + 3] == "#":
            print(k)
            print(t_map)    
            print("\n\n")
    except:
        pass
