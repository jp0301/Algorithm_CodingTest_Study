# 짝수와 홀수 구하기

def solution(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

    # A.1
    # return "Even" if num%2 ==0 else "Odd"

    # A.2
    # return ["Even", "Odd"][num & 1]

print(solution(0))