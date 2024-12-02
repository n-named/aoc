with open('input.txt', 'r') as f:
    input_data = [[int(num) for num in line.split(' ')] for line in f]


safe_cnt = 0

for rep in input_data:
    rep_dif = [rep[i+1]-rep[i] for i in range(len(rep)-1)]
    min_dif = min(rep_dif)
    max_dif = max(rep_dif)
    if ((min_dif >= 1) and (max_dif <= 3)) or ((min_dif >= -3) and (max_dif <= -1)):
        safe_cnt = safe_cnt +1


print(safe_cnt)
