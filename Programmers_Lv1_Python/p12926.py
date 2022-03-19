# 시저암호
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서
# 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다.
# "z"는 1만큼 밀면 "a"가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

def solution(s, n):

    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            # chr() 함수는 아스키코드 > 문자 / ord() 함수는 문자 > 아스키코드
            s[i] = chr( ( ord(s[i]) - ord('A') + n ) % 26 + ord('A') )
        elif s[i].islower():
            s[i] = chr( ( ord(s[i]) - ord('a') + n ) % 26 + ord('a') )
    
    return "".join(s)


print(solution('AB',1))
# A가 들어가면 (A - A + 1) % 26 + 65 = 66 = 아스키코드 66 = 'B'
print(solution('z',1))
print(solution('a B z',4))

