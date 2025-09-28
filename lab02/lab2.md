Function 1:
Analyze the following function with respect to number

```python
def function1(number):
	total = 0                   # 1 for 1 operator
	for i in range(number):     # number + 1
                                        # number for loop iterations
                                        # 1 more for range function
		x = i + 1           # 2(number) as there are two operators
		total += x * x      # 3(number) as there are 3 operators
 
	return total                # 1
```
T(n)=1+(number+1)+2(number)+3(number)+1
    =1+number+1+2number+3number+1
    = 3+6number
therefore, T(n)is O(n)

Function 2:
Analyze the following function with respect to number
```python

def function2(number):                                      
	return (number * (number + 1) * (2 * number + 1)) // 6  # 6 operators

```
T(n) = 6, 
therefore T(n) = O(1)

Function 3:
Analyze the following with respect to the length of the list. Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.

```python
def function3(list):
	n = len(list)                                  # 2 operators    
	for i in range(n - 1):                         # (n-1) + 1 + 1
		for j in range(n - 1 - i):                 # (n-1) + (n -2) + ...+ 2 + 1 + 3    
                                                        # ((n-1)*n/2) + 3
			if list[j] > list[j+1]:                # 4 operators
				tmp = list[j]                      # 2 operators    
				list[j] = list[j+1]                # 4 operators
				list[j + 1] = tmp                  # 3 operators
```

T(n) = 2 + (n-1) + 1 + 1 + ((n-1)*n/2) + 3 + 4 + 2 + 4 + 3
     = (n^2)/2 + n/2 + 20 
therefore, T(n) = O(n^2)


Function 4:
Analyze the following function with respect to number
```python
def function4(number):
	total = 1                                       # 1 operators
	for i in range(1, number):                      # (number-1) + 1
		total *= i + 1                              # 3(number-1)
	return total                                    # 1
```
T(n) = 1 + (number-1) + 1 + 3(number - 1) + 1
     = 1 + number - 1 + 1 + 3number - 3 + 1
     =  4number -1
therefore T(n) = O(n)