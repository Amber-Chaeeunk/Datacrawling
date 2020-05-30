print("BMI 계산기입니다.")
height = input("신장: ")
height = int(height)
weight = input("몸무게: ")
weight = int(weight)

print("BMI: ", (weight/(height*height)*10000))


