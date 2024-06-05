#출력하기 print()

birth_year=2000
print("출생연도:" + str(birth_year))
# 앞에 출생연도를 기준으로 뒤에 birth_year을 str으로 변경한


h = 10
m = 20
s = 30
print(h,m,s)
print(h,m,s,sep=':')
#공백대신 콜론 : 이 출력됨 / sep는 변수사이에 넣어야할 내용을 의미?!

price = 5000
print(price,"원") #이렇게 출력되는 것보단
print(price,"원",sep="") #이렇게 공백없이 출력해서 사용하는게 맞음 

#형변환으로 붙여서 출력해보기
print(str(price)+"원")
