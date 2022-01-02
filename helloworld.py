#Slicing 
jumin="971210-1234567"
print("성별:"+jumin[7])
print("연:"+jumin[0:2]) #0부터 2 직전까지  
print("생년원일:"+jumin[:6]) #처음부터 6 직전까지
                     #[7:] #7부터 끝까지
print("뒤 7자리(뒤에부터):"+jumin[-7:])
#맨 뒤에서 7번째부터 끝까지 (1234567을 의미)              

#문자열 처리 함수 
python="Python is Amazing"
print(python.lower()) #다 소문자로 처리
print(python.upper()) #대문자
print(python[0].isupper()) #0번째가 대문자냐
print(python.replace("Python","Java"))     

index=python.index("n") #어떤 문자가 어떤 위치에 있는지 확인
print(index)
index=python.index("n",index+1) #2번째 n을 찾는 것 
print(index)

print(python.find("n")) 
print(python.find("Java")) #없으면 -1
#print(python.index("Java")) #이건 없으면 오류가 남

print(python.count("n")) #n이 몇번 나오냐 