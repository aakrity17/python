# if __name__ == '__main__':
m=[]
s=[]
x=int(input())
for i in range(x):
    name=input()
    grade=float(input())
    m+=[[name,grade]]
    s+=[grade]
sl=(sorted(set(s)))[1]
for i,j in sorted(m):

    if j==sl:

            
        print(i)



    
