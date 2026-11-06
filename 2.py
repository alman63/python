x=[[1,2,3],[4,5,6],[6,7,8]]
k=2
result=[]
for i in range(1,len(x)):
    result.append([])
    for j in range(len(x)):
        if (k!=j):
            result[i-1].append(x[i][j])
print(result)