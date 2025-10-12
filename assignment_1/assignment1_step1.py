# Step1:
from cgitb import small


# question 1:
def bubble_sort(mylist):
    n = len(mylist)
    for i in range(n-1):
        swapped = False
        for j in range(n - 1 - i):
            if mylist[j] > mylist[j+1]:
                temporary_variable = mylist[j]
                mylist[j] = mylist [j + 1]
                mylist[j + 1] = temporary_variable
                swapped = True
        if not swapped:
            break
    return mylist

mylist = [7,9,1,2,3,6,5]
print(bubble_sort(mylist))



#  Question 2:
def selection_sort(mylist):
    n = len(mylist)
    for i in range( n - 1):
        smallest_value = i
        for j in range (i + 1, n):
            if mylist[j] < mylist[smallest_value]:
               smallest_value = j
        mylist[i], mylist [smallest_value] = mylist [smallest_value] , mylist[i]
    return mylist

mylist = [10,9,1,2,3,6,5]
print(selection_sort(mylist))



# Question 3:
def insertion_sort(mylist):
    n = len(mylist)
    for i in range (1,n):
        smallest_value = mylist[i]
        j = i - 1
        while j >=0 and mylist[j] > smallest_value:
            mylist[j+1] = mylist[j]
            j -= 1
        mylist[j + 1] = smallest_value
    return mylist

mylist = [10,9,1,2,3,6,5]
print(insertion_sort(mylist))

# Question 4:
def quick_sort(mylist):
    n = len(mylist)
    if n <= 1:
        return mylist
    pivot = mylist[0]
    left = [x for x in mylist[1:] if x <= pivot]
    right = [x for x in mylist[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

mylist = [10,9,1,2,3,6,5]
print(quick_sort(mylist))

# Question 5:
def insertion_sort_lr(mylist, left, right):
    n = len(mylist)
    for i in range(left + 1, right + 1):
        smallest_value = mylist[i]
        j = i - 1
        while j>= left and mylist[j] > smallest_value:
            mylist[j+1] = mylist[j]
            j = j - 1
            mylist[j+1] = smallest_value
    return mylist

mylist = [10,9,1,2,3,6,5]
left = 0
right = len(mylist) - 1
print(insertion_sort(mylist, left, right))

