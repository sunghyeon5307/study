# module

# 모듈? 함수, 변수, 클래스를 모아놓은 파이썬 파일 / 한 번 작성하면 계속해서 재사용 가능

# 사용법
# import 사용하여 '불러오기'가능
# import 사용 시 .py 생략(파일명만 작성)
# my.py를 불러와서 사용

import mymodule

print(mymodule.add(3, 5))
print(mymodule.sub(4, 2))

# from import
# from 모듈명 import 항목명
# : 특정 모듈에서 하나 이상의 특정 항목만 불러오기 가능
# 여러 항목 동시에 불러오는 경우 쉼표(,) 사용

from mymodule import greet, info
print(greet('냠'))
print(info('1000000'))

# import as
# : 모듈의 이름이 길거나 충돌 가능성 있을 때 사용
# as 키워드 사용하여 별칭 지정 가능

import mymodule as ha

print(ha.add(5, 7))
print(ha.sub(5, 7))

from mymodule import greet as zz
# mymodule 모듈 안의 greet 항목을 hello 별칭으로 사용
print(zz('냠냠'))