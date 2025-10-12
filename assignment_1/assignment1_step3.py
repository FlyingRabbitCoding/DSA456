import random
import copy

# Question 1
def bubble_sort(mylist):
    n = len(mylist)
    T = 0
    for i in range(n-1):
        swapped = False
        for j in range(n - 1 - i):
            T = T + 1
            if mylist[j] > mylist[j+1]:
                temporary_variable = mylist[j]
                mylist[j] = mylist [j + 1]
                mylist[j + 1] = temporary_variable
                T = T + 3
                swapped = True
        if not swapped:
            break
    return T

# Question 2
def selection_sort(mylist):
    n = len(mylist)
    T = 0
    for i in range( n - 1):
        T = T + 1
        smallest_value = i
        for j in range (i + 1, n):
            T = T + 1
            T = T + 1
            if mylist[j] < mylist[smallest_value]:
               smallest_value = j
        mylist[i], mylist [smallest_value] = mylist [smallest_value] , mylist[i]
        T = T + 3
    return T


# Question 3:
def insertion_sort(mylist):
    T = 0
    n = len(mylist)
    for i in range (1,n):
        smallest_value = mylist[i]
        j = i - 1
        while j >=0 and mylist[j] > smallest_value:
            T = T + 1
            mylist[j+1] = mylist[j]
            T = T + 1
            j -= 1
        mylist[j + 1] = smallest_value
        T = T + 1
    return T

# Question 4:
def quick_sort(mylist):
    T = 0
    n = len(mylist)
    if n <= 1:
        T = T + 1
        return mylist
    pivot = mylist[0]
    left = [x for x in mylist[1:] if x <= pivot]
    T = T + 1
    right = [x for x in mylist[1:] if x >= pivot]
    T = T + 1
    return T

# Question 5:
def insertion_sort_lr(mylist, left, right):
    T = 0
    n = len(mylist)
    for i in range(left + 1, right + 1):
        smallest_value = mylist[i]
        T = T + 1
        j = i - 1
        T = T + 1
        while j>= left and mylist[j] > smallest_value:
            T = T + 1
            mylist[j+1] = mylist[j]
            T = T + 1
            j = j - 1
            T = T + 1
            mylist[j+1] = smallest_value
            T = T + 1
    return T

def plot_tn_vs_n():
    sizes = [10, 50, 100, 500, 1000, 5000 ]
    sorts = {"bubble sort": bubble_sort, "selection sort": selection_sort, "insertion sort": insertion_sort, "quick sort": quick_sort, "insertion sort lr":insertion_sort_lr}
    for name, func in sorts.items():
        print(f"---{name}---")
        for n in sizes:
            variable_list = list(range(n,0,-1))
            if name == "insertion_sort_lr":
                result = func(variable_list.copy(), 0,len(variable_list)-1)
                T = result[0]
            else:
                T = func(variable_list.copy())
            print(f"list size {n}: T(n) = {T}")
        print()
plot_tn_vs_n()

# bubble_sort, insertion_sort, and selection_sort, the 3 sorts are takes more steps, it takes longer time. quick_sort and insertion_sort_lr the increase slowly.