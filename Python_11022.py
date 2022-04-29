"""문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 
각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. 
x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다."""

A=[]
B=[]
T = int(input(''))
for _ in range(T):
    a,b = list(map(int,input().split()))
    A.append(a)
    B.append(b)
for v in range(0,T):
    print(f"Case #{v+1}: {A[v]} + {B[v]} = {A[v]+B[v]} ")

