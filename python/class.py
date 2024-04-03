class Person:
    def i(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

levi = Person()
levi.i('tae', 20, '010-3333-7575', '경쥬')
print(levi.address)
print(levi.name)

class Calculator:
    # 수식 입력 -> 인스턴스 변수 expr에 저장
    def input_expr(self):
        expr = input('입력 >> ')
        self.expr = expr
    
    def calculate(self):
        # eval() : 문자열로 된 수식 자체 계산 함수
        return eval(self.expr)  

ha = Calculator()
ha.input_expr()
print('결과 {}임'.format(ha.calculate()))
