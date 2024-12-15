def search(gmap, crd, plant, plants, fences):
    plants.append(crd)
    ncrds = [[crd[0]-1, crd[1]], [crd[0], crd[1]+1], [crd[0]+1, crd[1]], [crd[0], crd[1]-1]]

    for ncrd in ncrds:
        if ncrd[0] < 0 or ncrd[1] < 0:
            fences = fences + 1
            continue
        try:
            if gmap[ncrd[0]][ncrd[1]] != plant:
                fences = fences + 1
                continue

            if gmap[ncrd[0]][ncrd[1]] == plant and (ncrd not in plants):
                plants, fences = search(gmap, ncrd, plant, plants, fences)
        except:
            fences = fences + 1
            
    return plants, fences


with open('input.txt', 'r') as f:
    input_data = f.read()

gmap = [list(row) for row in input_data.split("\n")]

revised = []

price = 0
for row in range(len(gmap)):
    for col in range(len(gmap[row])):
        if [row,col] in revised:
            continue
        
        plant = gmap[row][col]
        fences = 0
        plants = []

        plants, fences = search(gmap, [row,col], plant, plants, fences)
        
        revised.extend(plants)
        price = price + len(plants)*fences

print(price)
