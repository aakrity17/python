# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function  
a=int(input())
x=set(map(int,input().split()))
# print(x)
b=int(input())
y=set(map(int,input().split()))
w=sorted(x.symmetric_difference(y))
print(*w,sep='\n')
