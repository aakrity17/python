
from collections import deque
if __name__=='__main__':
    d=deque()
    n=int(input())
    for _ in range(n):  
        list=input().split()
        if list[0]=="append":
            d.append(list[1])
        elif list[0]=="appendleft":
            d.appendleft(list[1])
        elif list[0]=="pop":
            d.pop()
        elif list[0]=="popleft":
            d.popleft()
            #the answer will be in the form of the list so to print the answer without list use (*)
    print(*d)
