# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x=int(input())
# print(x)
li=list(map(int, input().split()))
d = Counter(li)
sum=0
cus=int(input())
for i in range(cus):
    ss,sp=input().split()
    ss=int(ss)
    sp=int(sp)
    if d[ss]!=0:
        sum=sum+sp
        # to update the no.of shoes left
        d[ss]-=1
print(sum)

