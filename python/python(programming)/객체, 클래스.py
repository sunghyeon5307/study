# 1. 클래스 붕어빵틀 = 서로 관련된 요소(변수 , 기능)들을 한곳에 모다 관리하기 위한 틀
# 2. 객체 : 클래스를 이용해 만들어진 실체
class bssm:
    def __init__(self, task, age, name):
        self.team = "부소마"
        self.task = task
        self.age = age
        self.name = name

    def intro(self):
        print("안녕하세요ㅗ, %s 에서 %s를 담당하고 있는 %d살 %s입니다. " %(self.team, self.task, self.age, self.name))
        
a = bssm("똥", 300, "김시연")
a.intro()
print(a)


class Grade:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def s_grade(self):
        if self.score >= 90:
            self.grade = "A"
        elif self.score >= 80:
            self.grade = "B"
        else:
            self.grade = "C"
    def __str__(self):
        return "%s: %c 등급" %(self.name, self.grade)
    
a1 = Grade("성현", 90)
a1.s_grade()
print(a1)

class FishCakeMaker:
    def __init__(self, **kwargs): # ** : 가변 인자 매개변수(몇개의 매개변수가 들어올지 모름)
        self.size = 10
        self.flavor = "팥"
        self.price = 100

        if "size" in kwargs:
            self.size = kwargs.get("size")
        if "flavor" in kwargs:
            self.flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self.price = kwargs.get("price")

    def show(self):
        print("붕어빵 크기{}".format(self.size))
        print("붕어빵 종류{}".format(self.flavor))
        print("붕어빵 가격{}".format(self.price))
        print("*"*30)

fish1 = FishCakeMaker()
fish2 = FishCakeMaker(size = 20, price = 300)
fish3 = FishCakeMaker(flavor = "초콜렛", size = 15)

fish1.show()
fish2.show()
fish3.show()


class MarketGoods(FishCakeMaker):
    def __init__(self, margin=1000, **kwargs):
        super().__init__(**kwargs)
        self.market_price = self.price + margin
    def show(self):
        print(self.flavor, self.market_price)

fish1 = MarketGoods(size=20, price=500)
fish1.show()





