#과제 1번
YEAR = int(input('연도를 입력하세요 : '))

if YEAR % 400 == 0:
    print("윤년입니다.")
elif YEAR % 100 == 0:
    print("평년입니다.")
elif YEAR % 4 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")


#과제 2번
N = int(input("임의의 숫자를 입력하시요 : "))
P = [0, 1]

for i in range(1, N - 1):
    P.append(P[i] + P[i - 1])
    
print(P[-1])