# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
s=set(map(int,input().split()))
n=int(input())
for i in range(n):
    # to take the commands in the form of list
    commands=input().split()
    if len(commands) > 1:
    # now as the list is in the form of integres so we need to get them in the form of int
        y=int(commands[1])
    if commands[0]=="pop":
        s.pop()
    if commands[0]=="remove":
        s.remove(y)
    if commands[0]=="discard":
        s.discard(y)
print(sum(s))
