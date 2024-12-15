def search(top_map, crd, ends):
    ncrds = [[crd[0]-1, crd[1]], [crd[0], crd[1]+1], [crd[0]+1, crd[1]], [crd[0], crd[1]-1]]
    for ncrd in ncrds:
        if ncrd[0] < 0 or ncrd[1] < 0:
            continue
        try:
            if top_map[ncrd[0]][ncrd[1]] - top_map[crd[0]][crd[1]] == 1:
                if top_map[ncrd[0]][ncrd[1]] == 9:
                    if ncrd not in ends:
                        ends.append(ncrd.copy())
                else:
                    search(top_map, ncrd, ends)
        except:
            pass
        

with open('input.txt', 'r') as f:
    input_data = f.read()

top_map = [[int(el) for el in list(row)] for row in input_data.split("\n")]

zeros = []
for row in range(len(top_map)):
    for col in range(len(top_map[row])):
        if top_map[row][col] == 0:
            zeros.append([row, col])

score = 0
for crd in zeros:
    ends = []
    search(top_map, crd, ends)
    score = score + len(ends)

print(score)
    
