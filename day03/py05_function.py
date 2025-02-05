# 함수, Function, Method, Procedure...
# def 함수명 (인자, ...):
#   함수안으로 진입

def say_hi():
    print('안녕~')
    return None

# print('인사하기:', end=' ')

def test(num, name):
    print(f'{num}명의 {name}이 있다.')
    return None

def say_hello(name):
    print(f'{name}야, 안녕!!')
    return None

def closing():
    return '바이바이~'

def get_age(birthYear):
    age = 2025 - birthYear
    return age

print('인사하기: ', end=' ')
say_hi()
say_hi()

name = input('이름입력 > ')
print('이름으로 인사하기:', end=' ')
say_hello(name)

year = int(input('생일년도 >'))
real_age = get_age(year)
print(f'나이는: {real_age}세')

print('작별인사 : ', closing())

