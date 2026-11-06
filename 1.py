x=[[1,0,0],[0,1,0],[0,0,1]]

def test(x):
    resultAll=0
    for i in range(1,len(x[0])):
        result=[]
        for t in range(1,len(x)):
            result.append([])
            for m in range(len(x)):
                if (i!=m):
                    result[t-1].append(x[t][m])

        resultAll+=(-1)**(i+1)*x[0][i-1]*test(result)
    return resultAll


print(test(x))

#i=1  x=[[5,6],[7,8]] 



# result = SUM((-1)**i+j*x[i][j]*test())