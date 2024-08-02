N = int(input())                            # 수열의 길이
A = [0]*N                                   # 수열을 저장할 리스트 초기화

for i in range(N):
    A[i] = int(input())                     # 주어진 수열 저장

stack = []                                  # 스택 초기화
num = 1                                     # 스택에 넣을 다음 숫자
result = True                               # 수열을 만들 수 있는지 여부를 판단할 변수
ans = ""                                    # 연산 기록을 저장할 문자열

for i in range(N):
    su = A[i]                               # 현재 처리 중인 수열의 숫자
    if su >= num:                           # 현재 수열의 숫자 >= 스택에 넣어야 할 다음 숫자
        while su >= num:                    # 수열의 숫자까지 스택에 숫자를 추가
            stack.append(num)               # 스택에 숫자를 추가
            num += 1                        
            ans += "+\n"                    # 푸시 연산 기록
        stack.pop()                         # 현재 숫자를 스택에서 제거 (목표 숫자 도달)
        ans += "-\n"                        # 팝 연산 기록
    else:                                   # 현재 수열의 숫자가 < 스택의 top 숫자
        n = stack.pop()                     # 스택의 top 숫자를 가져옴
        if n > su:                          # 스택의 top 숫자가 수열의 숫자보다 크면
            print("NO")                     # 해당 수열을 만들 수 없음 (수열 생성 불가능)
            result = False                  
            break                           # 반복문 종료
        else:                               # 스택의 top 숫자 = 수열의 숫자
            ans += "-\n"                    # 팝 연산 기록

if result:                                  # 수열 만들 수 있는 경우
    print(ans)                              # 연산 기록을 출력

    

#복습필요.....ㅠ