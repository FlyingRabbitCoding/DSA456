# Function 1:
# Analyze the following function with respect to the number.
from math import factorial

#
# def function1(value, number):
# 	if (number == 0):                                                 1
# 		return 1                                                      1
# 	elif (number == 1):                                               1
# 		return value                                                  1
# 	else:
# 		return value * function1(value, number-1)					  3 + factorial(n-1)
#
# T(n) = 1 + 1 + 1 + 1 + 3 + factorial(n-1)
# 	 = 7 + factorial(n-1)
# 	 = 7 + T(n-1)
# therefore, T(n) = O(n)

# Function 2:
# Analyze function2 with respect to the length of the mystring. Hint: you will need to set up two mathematical functions for operator counting. one for function2 and the other for recursive_function2

# def recursive_function2(mystring, a, b):
# 	if (a >= b):                                                                           1
# 		return True																		   1
# 	else:
# 		if (mystring[a] != mystring[b]):												   3
# 			return False																   1
# 		else:
# 			return recursive_function2(mystring, a + 1, b - 1)							   2 * n
#
#
# def function2(mystring):
# 	return recursive_function2(mystring, 0, len(mystring) - 1)							3
#
# 	T(n) = 1 + 1 + 3 + 1 + 3 + 2n
# 		 = 11 + 2n
# therefore T(n) = O

# part c reflection:

# Describe how to approach writing recursive functions; what steps do you take?
# step1: when does the recursion end,
# step2: how to call the function again

# Describe the process of analyzing recursive functions. How does it differ from analyzing non-recursive functions? How is it the same?
# needs to check how many operators and steps the functions will take.