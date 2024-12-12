with open('input.txt', 'r') as f:
    d_map = f.read()

blocks = []

is_frsp = 0
for i in range(len(d_map)):
    if not is_frsp:
        blocks.extend([str((int(i/2)))]*int(d_map[i]))
        is_frsp = 1
    else:
        blocks.extend(["."]*int(d_map[i]))
        is_frsp = 0

while '.' in blocks:
    last = blocks.pop()
    if last != '.':
        blocks[blocks.index('.')] = last

checksum = 0
for i in range(len(blocks)):
    checksum = checksum + int(blocks[i]) * i

print(checksum)
