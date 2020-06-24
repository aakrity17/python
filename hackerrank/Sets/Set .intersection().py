a=int(input())
roll=set(map(int,input().split()))
b=int(input())
rolls=set(map(int,input().split()))
# print(roll.intersection(rolls)) ;gives the output in the form of set
print(len(roll.intersection(rolls)))


