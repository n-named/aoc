with open('input.txt', 'r') as f:
    input_data = f.read()

mapg = [list(line) for line in input_data.split("\n")]

g = input_data.replace("\n", "").find("^")
g = [int(g / len(mapg[0])), int(g % len(mapg[0]))]

facing = "up"
fcs = ["up", "right", "down", "left"]

while 1:
    g_prev = g.copy()
    if facing == "up":
        g[0] = g[0]-1
    elif facing == "right":
        g[1] = g[1]+1
    elif facing == "down":
        g[0] = g[0]+1
    elif facing == "left":
        g[1] = g[1]-1
        
    mapg[g_prev[0]][g_prev[1]] = "X"
    
    if (g[0] < 0 or g[0] >= len(mapg)) or (g[1] < 0 or g[1] >= len(mapg[0])):
        break
    
    if mapg[g[0]][g[1]] == "#":
        facing = fcs[(fcs.index(facing) + 1) % len(fcs)]
        g = g_prev
        
mapg_t = "\n".join(["".join(line) for line in mapg])
poss_sum = mapg_t.count("X")
print(poss_sum)
