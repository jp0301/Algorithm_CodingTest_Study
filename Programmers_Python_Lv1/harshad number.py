# 하샤드 수 구하기

def solution(x):

    return x % sum([int(c) for c in str(x)]) == 0

print(solution(13))