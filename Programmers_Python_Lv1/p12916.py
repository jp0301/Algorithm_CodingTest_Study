# 12916 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916


def solution(s):
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            count1 += 1
        elif s[i] == "y" or s[i] == "Y":
            count2 += 1
  
    return True if count1==count2 else False


print(solution("pPoooyY"))
print(solution("Pyy"))

# return s.lower().count('p') == s.lower().count('y')