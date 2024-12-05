with open('input.txt', 'r') as f:
    input_data = f.read().split("\n\n")

rules = [rule.split("|") for rule in input_data[0].split("\n")]
updates = [update.split(",") for update in input_data[1].split("\n")]

corr_ids = []
for u in range(len(updates)):
    corr = 1
    for rule in rules:
        if (rule[0] in updates[u]) and (rule[1] in updates[u]):
            if updates[u].index(rule[0]) > updates[u].index(rule[1]):
                corr = 0
                break
    if corr:
        corr_ids.append(u)

mid_sum = sum([int(updates[i][int(len(updates[i])/2)]) for i in corr_ids])

print(mid_sum)
