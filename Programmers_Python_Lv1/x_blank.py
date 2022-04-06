def solution(x, n):

    answer = [x * i for i in range(1, n+1)]
    return answer

print(solution(-4, 2))


"""
Other solution 

def solution(x, n):
    answer = [i * x + x for i in range(n)]
    return answer
"""