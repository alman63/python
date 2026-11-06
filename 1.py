x=[[1,0,0],[0,1,0],[0,0,1]]

def test(x,i=0):
    print(x,'start')
    if len(x[0])==1: return x[0][i]
    resultAll=0
    for i in range(1,len(x[0])+1):
        result=[]
        for t in range(1,len(x)):
            result.append([])
            for m in range(len(x)):
                if (i!=m):
                    result[t-1].append(x[t][m])
        resultAll+=((-1)**(i))*x[0][i-1]*test(result,i)
    return resultAll


print(test(x))

#i=1  x=[[5,6],[7,8]] 
#  i - 1 -4(1,2,3)  r[]  t - 1-3(1,2)  r[[]]  m -0 -3(0,1,2)
# i=1 t=1 m=0 r[[0]]


# result = SUM((-1)**i+j*x[i][j]*test())