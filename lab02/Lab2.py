
# question 3
def fibonacci(n: int) -> int:
    sequence = (0, 1, 1, 2, 3, 5, 8, 13)

    if n < 0:
        return 0 # alternatively, throw an illegal exception here
    elif n <= len(sequence):
        return sequence[n]

    a = sequence[-2] # 2nd last value
    b = sequence[-1] # last value in sequence

    for _ in range(len(sequence), n + 1):
        a, b = b, a + b

    return b

# question 4
def sum_to_goal(num:list[int], goal:int)->int:
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j] == goal:
                return num[i] * num[j]
    return 0

# question 1, 2, 3 : I do not know, i am the only member in the group, there is no comparison at this moment
