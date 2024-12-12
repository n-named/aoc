with open('input.txt', 'r') as f:
    input_data = f.read()

rocks = [int(r) for r in input_data.split(" ")]

for clip in range(0, 25):
    rocks_t = []
    for r in range(len(rocks)):
        if rocks[r] == 0:
            rocks_t.append(1)

        elif len(str(rocks[r])) % 2 == 0:
            r_s = str(rocks[r])
            rocks_t.append(int(r_s[:int(len(r_s)/2)]))
            rocks_t.append(int(r_s[int(len(r_s)/2):]))

        else:
            rocks_t.append(rocks[r]*2024)
            
    rocks = rocks_t

print(len(rocks))
