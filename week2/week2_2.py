#입력연습하기

name = input("이름을 입력해주세요: ")
age = input("나이를 입력해주세요: ")    #input은 항상 str으로 인식
age = int(age)

print("이름은", name)
print("나이는", age)

g_age = age - 1
print("만 나이는", g_age)