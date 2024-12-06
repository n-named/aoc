import time


with open('input.txt', 'r') as f:
    input_data = f.read()

mapg_or = [list(line) for line in input_data.split("\n")]

g_or = input_data.replace("\n", "").find("^")
g_or = [int(g_or / len(mapg_or[0])), int(g_or % len(mapg_or[0]))]

facing = "u"
fcs = ["u", "r", "d", "l"]

mapg = [r[:] for r in mapg_or]
g = g_or.copy()

g_path = []
while 1:
    g_prev = g.copy()
    if facing == "u":
        g[0] = g[0]-1
    elif facing == "r":
        g[1] = g[1]+1
    elif facing == "d":
        g[0] = g[0]+1
    elif facing == "l":
        g[1] = g[1]-1
    if (g[0] < 0 or g[0] >= len(mapg)) or (g[1] < 0 or g[1] >= len(mapg[0])):
        break
    if mapg[g[0]][g[1]] == "#":
        facing = fcs[(fcs.index(facing) + 1) % len(fcs)]
        g = g_prev
        
    if g not in g_path:
        g_path.append(g.copy())

g_path.remove(g_or)

c_poss = 0
for obs in g_path:
    mapg = [r[:] for r in mapg_or]
    g = g_or.copy()
    facing = "u"
    
    mapg[obs[0]][obs[1]] = "#"
    
    start_time = time.time()
    while 1:
        g_prev = g.copy()
        if facing == "u":
            g[0] = g[0]-1
        elif facing == "r":
            g[1] = g[1]+1
        elif facing == "d":
            g[0] = g[0]+1
        elif facing == "l":
            g[1] = g[1]-1            
        if (g[0] < 0 or g[0] >= len(mapg)) or (g[1] < 0 or g[1] >= len(mapg[0])):
            break
        
        if facing == mapg[g[0]][g[1]] or (time.time() - start_time) > 0.01:
            c_poss = c_poss + 1
            break
        
        if mapg[g[0]][g[1]] == "#":
            facing = fcs[(fcs.index(facing) + 1) % len(fcs)]
            g = g_prev
            
        mapg[g_prev[0]][g_prev[1]] = facing

print(c_poss)
