import re


with open('input.txt', 'r') as f:
    input_data = f.read()

ants_map = [list(line) for line in input_data.split("\n")]
anod_map = [row[:] for row in ants_map]

frqs = list(set(list(input_data)))
frqs.remove(".")
frqs.remove('\n')

frqs_crds = {}

for frq in frqs:
    for line in range(len(ants_map)):
        for row in range(len(ants_map)):
            if frq == ants_map[line][row]:
                if frq in frqs_crds:
                    frqs_crds[frq].append([line, row])
                else:
                    frqs_crds[frq] = [[line, row]]
                    
    for crd0 in range(len(frqs_crds[frq])):
        for crd in range(len(frqs_crds[frq])-1):
            ant1 = frqs_crds[frq][crd0]
            ant2 = frqs_crds[frq][crd+1]
            if ant1 == ant2:
                break
            X1 = [2*ant1[0] - ant2[0], 2*ant1[1] - ant2[1]]
            X2 = [2*ant2[0] - ant1[0], 2*ant2[1] - ant1[1]]
            if (X1[0] >= 0 and X1[0] < len(anod_map)) and (X1[1] >= 0 and X1[1] < len(anod_map[0])):
                anod_map[X1[0]][X1[1]] = "#"
            if (X2[0] >= 0 and X2[0] < len(anod_map)) and (X2[1] >= 0 and X2[1] < len(anod_map[0])):
                anod_map[X2[0]][X2[1]] = "#"

unq_locs = len(re.findall("#", "\n".join(["".join(line) for line in anod_map])))
print(unq_locs)