import pandas as pd

input_data = pd.read_csv("input.txt", sep="\s+", header=None)

left = sorted(input_data[0])
right = sorted(input_data[1])


total_distance = 0
for i in range(len(left)):
    total_distance = total_distance + abs(left[i]-right[i])

print(total_distance)
