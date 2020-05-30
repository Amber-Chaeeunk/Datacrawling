players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]
print("현재 경기 중인 선수: ")
for i in players:
    print(i)

print("-"*50)
OUT = input("OUT 시킬 선수 번호: ")
OUT = int(OUT)
del players[OUT]

IN = input("IN 할 선수 이름: ")
players.append(IN)

print("-"*50)
print("교체 결과: ")
for i in players:
    print(i)