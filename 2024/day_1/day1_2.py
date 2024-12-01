import pandas as pd

input_data = pd.read_csv("input.txt", sep="\s+", header=None)

left = input_data[0].tolist()
right = input_data[1].tolist()


similarity_score = 0
for i in left:
    similarity_score = similarity_score + i*right.count(i)

print(similarity_score)
