import re
from math import floor, prod


with open('input.txt', 'r') as f:
    input_data = f.read().split("\n")

h = 103
w = 101
k = 100

quads= [0,0,0,0]
for robot in input_data:
    reg = re.findall("=(-?\d{,3}),(-?\d{,3})", robot)

    p = [int(reg[0][0]), int(reg[0][1])]
    v = [int(reg[1][0]), int(reg[1][1])]

    kpv = [k*v[0], k*v[1]]

    crd = [p[0] + kpv[0], p[1] + kpv[1]]
    crd[0] = crd[0]%w
    crd[1] = crd[1]%h

    if crd[0] < floor(w/2) and crd[1] < floor(h/2):
        quads[0] = quads[0] + 1
    elif crd[0] > int(w/2) and crd[1] < floor(h/2):
        quads[1] = quads[1] + 1
    elif crd[0] < floor(w/2) and crd[1] > int(h/2):
        quads[2] = quads[2] + 1
    elif crd[0] > int(w/2) and crd[1] > int(h/2):
        quads[3] = quads[3] + 1

print(prod(quads))
