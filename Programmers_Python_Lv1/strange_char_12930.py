# 이상한 문자 만들기 12930문제
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    
    a = s.split(" ")

    for i in range(len(a)):
        char = list(a[i])

        for j in range(len(char)):
            if (j % 2) == 0:
                char[j] = char[j].upper()
            else:
                char[j] = char[j].lower()

        a[i] = "".join(char)
        
    return " ".join(a)

    """
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
    """


print(solution("try hello world"))