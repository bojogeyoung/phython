num = 3
sort = "coffee"
print("나는 오늘 %d잔의 " %num,end="")
print("%s를 마셨다" %sort)

#다른 방법
print("나는 오늘 %d잔의 %s를 마셨다" %(num,sort))
 
 


#f문자열 ~ 포매팅 사용할 때 f접두사 뒤에 칸을 띄우고 문자열을 입력하면 오류발생
name = "홍길동"
age = 20
print(f"나의 이름은 {name}입니다. 나이는 {age}살 입니다.")
print(f"10년 후에 {age+10}살이 됩니다.")
