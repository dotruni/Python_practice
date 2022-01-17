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

