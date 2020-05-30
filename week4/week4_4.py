#openpyxl 연습하기

import openpyxl

wb = openpyxl.Workbook() #워크북 만들기
sheet = wb.active  #현재 활성화 된 시트 선택
sheet['A1'] = "Hello World"  #A1자리는 셀번호 -> 셀번호 무조건 알아야함
sheet.cell(row=3, column=3).value = "Good Bye"  #셀번호 모를 때 직접 원하는 위치에 넣을 수 있음

sheet.append(["Python", "Java", "HTML", "JAVASCRIPT"])  #append는 지금 내가 열고있는 엑셀의 가장 아래의 행에 데이터 추가해줌
sheet.append(["Coala", "study", "Crawling"])
wb.save("test.xlsx") #워크북 이름 만들기
