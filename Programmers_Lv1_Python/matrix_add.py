def solution(A, B):

    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer


    # 출력 확인용
    print(solution([[1,2], [2,3]], [[3,4],[5,6]]))