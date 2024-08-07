import sys
input = sys.stdin.readline
result = 0  # swap 결과값 저장할 변수

# 병합 정렬 수행 함수
def merge_sort(s, e):
    global result

    if e - s < 1:
        return  # 배열의 크기가 1 이하일 경우 함수 종료
    m = int(s + (e - s) / 2)  # 중간 인덱스 계산
    merge_sort(s, m)  # 좌측 부분 배열 정렬
    merge_sort(m + 1, e)  # 우측 부분 배열 정렬

    # 임시 배열에 현재 배열 상태 저장
    for i in range(s, e + 1):
        tmp[i] = A[i]

    k = s
    index1 = s
    index2 = m + 1

    # 두 부분 배열을 병합
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:  # 좌측 배열 값이 우측 배열 값보다 클 경우
            A[k] = tmp[index2]
            result = result + index2 - k  # swap 횟수 계산
            k += 1
            index2 += 1
        else:  # 좌측 배열 값이 우측 배열 값보다 작을 경우
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    # 남은 좌측 배열 값을 결과 배열에 추가
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1

    # 남은 우측 배열 값을 결과 배열에 추가
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

# 입력 처리
N = int(input())  # 배열 크기 입력
A = list(map(int, input().split()))  # 배열 값 입력
A.insert(0, 0)  # 배열의 인덱스를 1부터 사용하기 위해 0번째에 0 추가
tmp = [0] * int(N + 1)  # 임시 배열 생성

# 병합 정렬 수행
merge_sort(1, N)

# 결과 출력
print(result)
