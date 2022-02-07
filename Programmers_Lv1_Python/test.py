from math import sqrt
def solution(n):

    if  int(sqrt(n)) == sqrt(n):
        return pow(sqrt(n) + 1, 2)
    else:
        return -1


print(solution(121))