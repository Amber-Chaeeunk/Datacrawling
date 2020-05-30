pay = input("최저시급을 입력해주세요: ")    #input으로 입력받은 것은 모두 character
pay = int(pay)

if pay > 8350:
    print("적절한 시급입니다.")
else:
    print("최저임금보다 적어요.")


numbers = [1,3,5,6,8,9,10]

for n in numbers:
    if (n <= 5) and (n%2==0):
        print(n)
    else:
        print(n, "*")

articles = ["손흥민은 손으로 상대의 얼굴을 밀며 맞받아쳤다.", "AS로마의 니콜로 자니올로", "이강인의 팀 동료 페란 토레스"]

for a in articles:
    if "손흥민" in a:
        print("손흥민 기사")
    elif "이강인" in a:
        print("이강인 기사")
    else:
        print("손흥민/이강인이 나오지 않는 기사")