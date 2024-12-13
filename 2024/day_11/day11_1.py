with open('input.txt', 'r') as f:
    input_data = f.read()

stones = [int(s) for s in input_data.split(" ")]

for clip in range(0, 25):
    stones_t = []
    for s in range(len(stones)):
        if stones[s] == 0:
            stones_t.append(1)

        elif len(str(stones[s])) % 2 == 0:
            s_s = str(stones[s])
            stones_t.append(int(s_s[:int(len(s_s)/2)]))
            stones_t.append(int(s_s[int(len(s_s)/2):]))

        else:
            stones_t.append(stones[s]*2024)
            
    stones = stones_t

print(len(stones))
