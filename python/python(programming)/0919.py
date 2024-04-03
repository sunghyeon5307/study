print("a"+"b")
print("a","b")
print("나는 {}을 좋아해요.".format("빨간색"))
print("{1}색과 {0}색을 좋아해요.".format("파란","빨강"))

def 함수명():
    return

a = 5 # 전역변수
def func():
    a = 3 # 지역변수
    return a
print(func())
print(a)

def profile(name, age=17, language="python"):
    print("이름: {0}\t나이: {1}\t 주사용언어{2}".format(name,age,language))
profile(language="python", age=20, name="유재석")

def func(*a):
    print(type(a))
    return sum(a)
func(1,2,3)