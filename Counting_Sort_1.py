arr = [1,1,3,2,17,8,9,6,4,4,5,6,88,4,3,3,2,23,42,53,3,45,3,45,45,56,75,7]

counter = [0] * 100

for i in arr:
    counter[i] += 1

print(counter)
