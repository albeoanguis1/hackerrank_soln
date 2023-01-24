lst_2d = [[1,2,3],
        [4,5,6],
        [7,8,9]]

leftsum = 0
rightsum = 0

i = 0
j = 0

while ( i < len(lst_2d)):
    # print(lst_2d[i][j])
    leftsum += lst_2d[i][j]
    i+=1
    j+=1

i = 0
j = len(lst_2d)-1

while (i < len(lst_2d)):
    # print(lst_2d[i][j])
    rightsum += lst_2d[i][j]
    i += 1
    j -= 1

print(abs(leftsum - rightsum))
