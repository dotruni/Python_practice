#계속 헷갈리기 때문에 끊임 없이 복습!

#1. 자료형 
# 자료에 대한 타입 : 숫자, 문자열, 불
# 어떤 값을 담는 자료구조: 변수, 리스트, 튜플, 딕셔너리, 집합

#1)숫자 : 정수(int), 실수(float), 컴퓨터식 지수 표현 방식 ex) 4.24e10 (float),8진수,16진수 
a=1
print(type(a)) #int #정수
#숫자형으로 사칙연산
#곱하기 : * , 나누기: /, 몫: // , 나머지: % , 제곱: **

#2)문자열 (str) : string 
a= 'Python\'s fravorite food is perl'
print(a) #여기서 \'이거는 문자열 따옴표다라고 말해줄 수 있음.

a= 'Life is too short\n You need python'
print(a)

#escape 문자 \n: 문자열 안에 줄을 바꿀 때 사용, \t:간격 ,\\:그대로 표현할 때
#그러니까 \(빽슬래쉬)는 이거는 문자 그대로다 말하는 도구

#여러 줄로 이루어진 문자열 : "" 3개나 '' 3개를 이용하면 좋다
multiline=''' 
Life is too short
You need python'''
print(multiline)

hello="""
I think
I am too hot"""
print(hello)

#인덱싱  a[ 이상:미만 :간격 ]
a="12345678"
print(a[2:6:2])  
#formating %s %d
a="%0.4f"%3.42433242324 
#%간격.소수점 남기는 자리 수f
print(a)

a= "hobby"
print(a.count('b')) #b가 몇번 나왔냐
print(a.find('b')) #가장 처음 나온 b의 위치는 ? #없으면 -1 나옴

a=[1,3,4,6,7,0,7,8]
#a.append
#a.sort
#a.insert(0,4)
#a.remove(1)
#a.extend

#리스트-> 서랍장 같은 것 
#튜플은 삭제할 수 없음, 리스트는 삭제 가능. (append 이런거 x)
#: 변화시키는 건 안되는데 보는 것은 된다, 사칙연산도 가능, 하지만 변하지는 않음.

#딕셔너리 : API에 자주 활용됨 EX) JSON
dic={'name':'Eric','age':15}
a={1 :'a'}
a['name']="익명"
print(a)
#key 하고 value이기 때문에 key는 중복되면 X
a={1:'나 자신', 2:'내 건강', 3:'내 꿈', 4:'사랑'}
print(a.keys())
print(a.values())
print(a.items()) #튜플 형태로

 #활용 예시
for v in a.values():
     print(v)

a.clear() #딕셔너리 지우기
print(a.get(4,'없음')) 
print(4 in a ) #a에 4가 있냐

