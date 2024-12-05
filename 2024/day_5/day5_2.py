with open('input.txt', 'r') as f:
    input_data = f.read().split("\n\n")

rules = [rule.split("|") for rule in input_data[0].split("\n")]
updates = [update.split(",") for update in input_data[1].split("\n")]

incorr_ids = []
for u in range(len(updates)):
    is_incorr = 0
    is_incorr_rule = 1
    while is_incorr_rule:
        for rule in rules:
            if (rule[0] in updates[u]) and (rule[1] in updates[u]):
                i1 = updates[u].index(rule[0])
                i2 = updates[u].index(rule[1])
                if i1 > i2:
                    updates[u][i1], updates[u][i2] = updates[u][i2], updates[u][i1]
                    is_incorr = 1                     
                else:
                    is_incorr_rule = 0
                     
        for rule in rules:
            if (rule[0] in updates[u]) and (rule[1] in updates[u]):
                if updates[u].index(rule[0]) > updates[u].index(rule[1]):
                    is_incorr_rule = 1
                    break
                
    if is_incorr:
        incorr_ids.append(u)

mid_sum = sum([int(updates[i][int(len(updates[i])/2)]) for i in incorr_ids])

print(mid_sum)
