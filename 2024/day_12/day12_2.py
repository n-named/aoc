def f_add(ncrd, ncrds, crd, fences):
    if ncrd == 1 or ncrd == 3:
        k = (ncrds[ncrd][1] + crd[1])/2
        if ncrd == 1:
            k = k-150
        if k in fences[0]:
            fences[0][k].append(ncrds[ncrd][0])
        else:
            fences[0][k] = [ncrds[ncrd][0]]
    else:
        k = (ncrds[ncrd][0] + crd[0])/2
        if ncrd == 0:
            k = k-150
        if k in fences[1]:
            fences[1][k].append(ncrds[ncrd][1])
        else:
            fences[1][k] = [ncrds[ncrd][1]]

    return fences


def search(gmap, crd, plant, plants, fences):
    plants.append(crd)
    ncrds = [[crd[0]-1, crd[1]], [crd[0], crd[1]+1], [crd[0]+1, crd[1]], [crd[0], crd[1]-1]]

    for ncrd in range(4):
        if ncrds[ncrd][0] < 0 or ncrds[ncrd][1] < 0:
            fences = f_add(ncrd, ncrds, crd, fences)
            continue
        try:
            if gmap[ncrds[ncrd][0]][ncrds[ncrd][1]] != plant:
                fences = f_add(ncrd, ncrds, crd, fences)
                continue

            if gmap[ncrds[ncrd][0]][ncrds[ncrd][1]] == plant and (ncrds[ncrd] not in plants):
                plants, fences = search(gmap, ncrds[ncrd], plant, plants, fences)
        except:
            fences = f_add(ncrd, ncrds, crd, fences)

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
        fences = [{},{}]
        plants = []

        plants, fences = search(gmap, [row,col], plant, plants, fences)
        
        revised.extend(plants)
        
        f_cnt = 0
        for hv in fences:
            for k in hv:
                f_crdrs = sorted(hv[k])
                if len(f_crdrs) == 1:
                    f_cnt = f_cnt +1
                    continue
                
                for f_crd in range(len(f_crdrs)-1):
                    if f_crdrs[f_crd+1] - f_crdrs[f_crd] > 1:
                        f_cnt = f_cnt +1
                    if f_crd+1 == len(f_crdrs)-1:
                        f_cnt = f_cnt +1

        price = price + f_cnt * len(plants)

print(price)
