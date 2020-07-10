import math
import os
import random
import re
import sys

def Calculate(arr,i,j):
    a=arr[i][j]
    b=arr[i][j+1]
    c=arr[i][j+2]
    e=arr[i+1][j+1]
    d=arr[i+2][j]
    f=arr[i+2][j+1]
    g=arr[i+2][j+2]
    return (a+b+c+d+e+f+g)

if __name__ == "__main__":
    arr=[]
    for _ in range(6):
        arr.append(list(map(int,input().split())))
    res=[]
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum=Calculate(arr,i,j)
            res.append(sum)
    print(max(res))






     
            
