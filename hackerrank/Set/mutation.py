n=int(input())
A = set(map(int,input().split()))
other = int(input())
for i in range(other):
    x,y= input().split()
    li=set(map(int,input().split()))
    eval("A.{0}({1})".format(x,li))
print(sum(A))
    
    
