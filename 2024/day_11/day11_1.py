with open('input.txt', 'r') as f:
    input_data = f.read()

stones = [int(r) for r in input_data.split(" ")]

for clip in range(0, 25):
    stones_t = []
    for r in range(len(stones)):
        if stones[r] == 0:
            stones_t.append(1)

        elif len(str(stones[r])) % 2 == 0:
            r_s = str(stones[r])
            stones_t.append(int(r_s[:int(len(r_s)/2)]))
            stones_t.append(int(r_s[int(len(r_s)/2):]))

        else:
            stones_t.append(stones[r]*2024)
            
    stones = stones_t

print(len(stones))
