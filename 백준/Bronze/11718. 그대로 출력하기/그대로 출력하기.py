import sys

# sys.stdin = 표준 입력을 파일처럼 읽을 수 있는 객체
for line in sys.stdin:    #입력이 EOF될때까지 반복
    print(line.strip())