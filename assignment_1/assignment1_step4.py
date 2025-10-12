import random
import copy
import time

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

sizes = [10, 50, 100, 500, 1000, 5000 ]
bubble_times = []
selection_times = []
insertion_times = []
quick_times = []
insertion1_times = []

for size in sizes:
    test_list = list(range(size, 0, -1))

    # bubble_sort
    variable_list_copy = copy.deepcopy(test_list)
    start = time.time()
    bubble_sort(variable_list_copy)
    end = time.time()
    bubble_times.append(end - start)

    #  selection_sort
    variable_list_copy = copy.deepcopy(test_list)
    start = time.time()
    selection_sort(variable_list_copy)
    end = time.time()
    selection_times.append(end - start)

    #   insertion_sort
    variable_list_copy = copy.deepcopy(test_list)
    start = time.time()
    insertion_sort(variable_list_copy)
    end = time.time()
    insertion_times.append(end - start)

    #   quick_sort
    variable_list_copy = copy.deepcopy(test_list)
    start = time.time()
    quick_sort(variable_list_copy)
    end = time.time()
    quick_times.append(end - start)

    #   insertion_sort_lr
    # variable_list_copy = copy.deepcopy(test_list)
    # start = time.time()
    # insertion_sort_lr(variable_list_copy)
    # end = time.time()
    # insertion1_times.append(end - start)


print("list size:", sizes)
print("bubble sort time: ", bubble_times)
print("selection sort: ", selection_times)
print("insertion sort: ", insertion_times)
print("quick sort: ", quick_times)
# print("insertion_sort_lr: ", insertion1_times)