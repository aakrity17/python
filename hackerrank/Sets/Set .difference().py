a=int(input())
roll=set(map(int,input().split()))
b=int(input())
rolls=set(map(int,input().split()))
print(len(roll.difference(rolls)))
