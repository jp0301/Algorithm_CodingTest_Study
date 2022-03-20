# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    s = list(s)

    for i in range(len(s)):
        s[i] = ord(s[i])
        
    s.sort(reverse=True)

    for i in range(len(s)):
        s[i] = chr(s[i])
    
    return "".join(s)

print(solution("Zbcdefg"))

# 한줄 풀이
# return ''.join(sorted(s, reverse=True))
