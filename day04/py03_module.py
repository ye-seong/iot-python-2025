# 모듈 - 레고
# 파이썬 파일 하나가 모듈 하나
# 모듈사용 하려면
# import 모듈명 - 기본
# from 모듈명 import 상세...
import py02_car

hisCar = py02_car.Car('기아차', '스팅거', '몰라')
print(hisCar)

import py02_car as c

herCar = c.Car('페라리', 'GT911', '290너2468')
print(herCar)

from py02_car import Car

thatCar = Car('람보르기니', '이름몰라', '58로1004')
