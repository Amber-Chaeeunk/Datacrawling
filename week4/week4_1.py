# print("hello world")
# print("goodbye")
#
# f = open("test.txt", "w")
# f.write("hello world\n")
# f.write("goodbye")
# f.close()

f = open("company.csv","w",encoding="UTF-8")
# f.write("회사이름", "색상\n")

name = ["카카오", "네이버", "삼성", "sk"]
color = ["노랑", "초록", "파랑", "빨강"]

for i in range(len(name)):
      f.write(name[i] + ',' + color[i] + '\n')

f.close()
