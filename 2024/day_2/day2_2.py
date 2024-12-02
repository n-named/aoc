with open('input.txt', 'r') as f:
    input_data = [[int(num) for num in line.split(' ')] for line in f]


safe_cnt = 0

for rep in input_data:
    rep_dif = [rep[i+1]-rep[i] for i in range(len(rep)-1)]
    min_dif = min(rep_dif)
    max_dif = max(rep_dif)
    if ((min_dif >= 1) and (max_dif <= 3)) or ((min_dif >= -3) and (max_dif <= -1)):
        safe_cnt = safe_cnt +1
    else:
        for rem in range(len(rep)):
            test_rep = rep.copy()
            test_rep.pop(rem) 
            rep_dif = [test_rep[i+1]-test_rep[i] for i in range(len(test_rep)-1)]
            min_dif = min(rep_dif)
            max_dif = max(rep_dif)
            if ((min_dif >= 1) and (max_dif <= 3)) or ((min_dif >= -3) and (max_dif <= -1)):
                safe_cnt = safe_cnt +1
                break


print(safe_cnt)
