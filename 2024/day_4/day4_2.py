with open('input.txt', 'r') as f:
    input_data_t = f.read()


m = [list(line) for line in input_data_t.split("\n")]

ap = 0

for r in range(1, len(m)-1):
    for c in range(1, len(m[0])-1):
        if m[r][c]=="A":
            if m[r-1][c-1]==m[r+1][c-1]=="M" and m[r-1][c+1]==m[r+1][c+1]=="S":
                ap = ap + 1
            elif m[r-1][c+1]==m[r-1][c-1]=="M" and m[r+1][c+1]==m[r+1][c-1]=="S":
                ap = ap + 1
            elif m[r-1][c-1]==m[r+1][c-1]=="S" and m[r-1][c+1]==m[r+1][c+1]=="M":
                ap = ap + 1
            elif m[r-1][c+1]==m[r-1][c-1]=="S" and m[r+1][c+1]==m[r+1][c-1]=="M":
                ap = ap + 1

print(ap)
