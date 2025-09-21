# Question1:
def wins_rock_scissors_paper(player1:str, player2:str) -> bool:
    player1 = player1.lower()
    player2 = player2.lower()

    if player1 == "rock" and player2 == "scissors":
        return True
    elif player1 == "paper" and player2 =="rock":
        return True
    elif player1 == "scissors" and player2 =="paper":
        return True
    else:
        return False

# Question2:
def factorial(number:int)->int:
    total = 1
    if number == 0:
        return 1
    for i in range(1, number+1):
        total *= i
    return total

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

