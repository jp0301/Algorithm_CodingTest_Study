# 정수 제곱근 판별

def solution(n):

    if n ==  0:
        x = n **(1/2)
        return (x+1)**2
    else:
        return -1


print(solution(3))