
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
eng=set(map(int,input().split()))
b=int(input())
french= set(map(int,input().split()))
print(len(eng.union(french)))
