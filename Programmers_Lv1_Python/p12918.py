# 12918 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918


def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False

# return s.isdigit() and len(s) in (4, 6)

print(solution("a1234"))
print(solution("1234"))
