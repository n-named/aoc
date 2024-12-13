import functools


@functools.cache
def count(blinks, num, s_cnt):
    blinks = blinks + 1
    if blinks == 76:
        return 1

    s_num = str(num)
    len_num = len(s_num)
    if num == 0:
        num = 1
        s_cnt = count(blinks, num, s_cnt)
    
    elif len_num % 2 == 0:
        num = int(s_num[:int(len_num/2)])
        s_cnt = count(blinks, num, s_cnt)

        num = int(s_num[int(len_num/2):])
        s_cnt = s_cnt + count(blinks, num, s_cnt)
        
    else:
        num = num*2024
        s_cnt = count(blinks, num, s_cnt)

    return s_cnt


with open('input.txt', 'r') as f:
    input_data = f.read()

stones = [int(s) for s in input_data.split(" ")]

blinks = 0
s_cnt = 0
for num in stones:
    s_cnt = s_cnt + count(blinks, num, s_cnt)

print(s_cnt)
