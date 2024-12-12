with open('input.txt', 'r') as f:
    d_map = f.read()

blocks = []

is_frsp = 0
for pos in range(len(d_map)):
    if not is_frsp:
        blocks.append([(int(pos/2))]*int(d_map[pos]))
        is_frsp = 1
    else:
        blocks.extend(["."]*int(d_map[pos]))
        is_frsp = 0

try:
    for end_pos in range(1, len(blocks)+1):
        cur_blc = blocks[-end_pos]
        if set(cur_blc) != {"."}:
            for pos in range(len(blocks)-end_pos):
                try:
                    if set(blocks[pos:pos+len(cur_blc)]) == {'.'}:
                        blocks[pos:pos+len(cur_blc)], blocks[-end_pos] = [cur_blc], blocks[pos:pos+len(cur_blc)]
                        break
                except:
                    pass
except:
    pass

blocks = [item for row in blocks for item in row]

checksum = 0
for pos in range(len(blocks)):
    if blocks[pos] != ".":
        checksum = checksum + int(blocks[pos]) * pos

print(checksum)
