from statistics import mean
def average(array):
    st=set(array)
    return mean(st)

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
