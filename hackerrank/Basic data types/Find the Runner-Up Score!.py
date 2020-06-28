if __name__ == '__main__':
    n = int(input())
# map() takes two arguments: A function and a list. In this case the function is int, and the list is the one from above. It executes the function once on each thing in the list, and returns the result. In this casse the function is int, which converts its argument to an integer (a whole number).

# list() converts its argument to a list.
    arr = list(map(int, input().split()))

    list1=[]

    for i in arr:

         if i not in list1:


                    list1.append(i)

    list1.sort(reverse=True)
    # reverse function sorts the list in the descending order

    print(list1[1])
