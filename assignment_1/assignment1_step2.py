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


def test_t():
    import random
    import copy

    best_case = list(range(100))
    worst_cast = list(range(100, -1, -1))
    average_case = [random.randint(1, 100) for _ in range(10)]

    three_scenario = {"best case": best_case, "worst case": worst_cast, "average case": average_case}
    sorts = {"bubble sort": bubble_sort, "selection sort": selection_sort, "insertion sort": insertion_sort, "quick sort": quick_sort, "insertion sort lr":insertion_sort_lr}

    for name, func in sorts.items():
        print(f"---{name}---")
        for scenario_name, variable_list in three_scenario.items():
            test_list = copy.deepcopy(variable_list)
            if name == "quick sort":
                T = func(test_list)
            else:
                T = func(test_list)
            print(f"{scenario_name}: T(n) = {T}")
        print("")

test_t()


