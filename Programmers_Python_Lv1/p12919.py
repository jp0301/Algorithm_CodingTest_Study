# 12919 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))

def solution2(seoul):
    for index, name in enumerate(seoul):
        if name == "Kim":
            answer = "김서방은 " + str(index) + "에 있다"
    return answer

print(solution(["Jane","Kim"]))
print(solution2(["Jane","Kim"]))