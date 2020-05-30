#for문 이용한 반복문
MAX = 10

#한개 들어가있는 경우 (0이상, 그 수 미만)
for i in range(MAX):
    print(i)
    print("반복문을 배워 봅시다.")

#두개 들어가있는 경우 (첫번째 수 이상, 마지막 수 미만)
for i in range(1, MAX):
    print(i)
    print("반복문을 배워 봅시다.")

#세개 들어가있는 경우 (첫번째 수 이상, 마지막 수 미만, 건너뛰면서)
for i in range(1, MAX, 2):
    print(i)
    print("반복문을 배워 봅시다.")

#in range 활용해서 리스트 반복
players = ["황의조", "황의찬", "구자철", "이재성", "기성용"]
print("2019년 아시안컵 출전명단:")

for i in range(4):
    print(players[i])

print("2019년 아시안컵 출전명단:")
for i in range(len(players)):
    print(players[i])

#in 리스트를 활용하여 리스트 반복
players = ["황의조", "황의찬", "구자철", "이재성", "기성용"]

print("2019년 아시안컵 출전명단")
for p in players:
    print(p)