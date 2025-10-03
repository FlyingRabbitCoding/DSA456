# Function 1:
# This function is passed a number and returns(number)! = (number)(number-1)(number-2)...(3)(2)(1). By definition, 0! = 1

def factorial(number):
    if number == 0:
        return 1
    else:
        return number*(factorial(number-1))
#
# print(factorial(2))

# Function 2:
# Write the RECURSIVE function linear_search. linear_search() is passed a list of values and a key. If a matching key is found in the list, the function returns the index of where the key was found. If the key is not found, the function returns -1.

def linear_search(list,key):
    total_num = int(len(list))
    for i in range(total_num):
        if list[i] == key:
            return i
    else:
        return -1

#
# list1 = [1,2,3,4,5,6]
# print(linear_search(list1,1))


# Function 3:
# Write the RECURIVE function binary_search. binary_search() is passed a sorted list of values and a key. If a matching key is found in the list, the function returns the index of where the key was found. If the key is not found, the function returns -1.

def binary_search(list, key):
    left = 0
    right = len(list) -1
    while left <= right:
        mid = (left + right ) // 2
        if list[mid] == key:
            return mid
        if list[mid] <= key:
            left = mid + 1
        else:
            right = mid - 1
    return -1













