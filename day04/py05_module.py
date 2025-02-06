# 외부 모듈을 사용하기 위한 방법
# 내 컴퓨터에 없는 모듈을 가져와서 사용하려면
# pip : 파이썬 제공하는 Package Installer of Python
# https://pypi.org 에서 설치할 패키지 검색색

import requests

print('외부 패키지 사용')

# 웹 브라우저가 아닌 파이썬 상에서 웹사이트 접속
res = requests.get('https://www.google.com') # website URL

print(res.status_code) # 200(OK)
# print(res.content)

f = open('./day04/index.html', mode='w', encoding='utf-8')
f.write(str(res.content, 'utf-8'))
f.close()

print('파일생성!')

class Sample:
    pass

sam = Sample()
print(sam)

class Sample:
    pass

import py02_car as c

## __main__ 프로그램이 시작하는 진입점 (entry point) 지칭
# C언어등의 static void main()와 동일한 역할
# 폴더 안에 py파일 중 실행되는 파이썬 파일이 __main__(진입점)이 되고
# 나머지는 모듈이 됨됨
if __name__ == '__main__':
    sam = Sample()
    print(sam)
    print(__name__)
    car = c.Car()