x=[[1,2],[4,5]]
k=1
result=[]
for t in range(1,len(x)):
    result.append([])
    for m in range(len(x)):
        if (k!=m):
            result[t-1].append(x[t][m])
print(result)