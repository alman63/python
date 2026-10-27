x =[[0,0,6,0],[0,1,0,0],[0,0,0,0],[0,0,15,0]]
s=0
#Max = max(1,5,9)=9
maxArray=x[0][0]
for i in range(len(x)):
    maxI=x[0][0]
    for j in range(i+1):
        for key in range(i+1):
            if maxI <x[0:i+1][j][key]:
                maxI=x[0:i+1][j][key]
    s+=maxI
print(s)
