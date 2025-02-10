from tkinter import * # tkinter 모듈의 모든 함수와 클래스를 쓸 수 있음
import tkinter.font as fnt

root = Tk()
root.geometry('600x200')
root.title('카운트 예제') # 윈도우 창 제목변경

# 이벤트
count = 0 # 계속 증가시킬 수를 담는 변수

def countUp():
    global count # 전역변수 count를 함수내에서 사용할 거야!
    count += 1
    label['text'] = f'버튼 클릭: {count}' # 라벨에 표시

def countInit():
    global count
    count = 0
    label['text'] = f'버튼 클릭: 0' # 라벨에 표시

myfont = fnt.Font(family='NanumGothic', size=20)

# 숫자카운트를 표시할 라벨
label = Label(root, text='버튼 클릭: 0', fg='blue', font=myfont)
# side = LEFT, TOP, RIGHT, BOTTOM
# padding = 안쪽 여백, padx(왼쪽, 오른쪽에 여백), pady(위, 아래 여백)
label.pack(side=TOP, pady=20)
# 버튼, command 파라미터 - 이벤트 함수를 정의
buttonUp = Button(root, text='카운트', font=myfont, command=countUp) # countUp이라는 함수가 마우스 클릴때마다 실행
buttonUp.pack(side=LEFT, padx=20, pady=20)
buttonInit = Button(root, text='초기화', font=myfont, command=countInit) # countInit 함수가 실행
buttonInit.pack(side=RIGHT, padx=20, pady=20)

root.mainloop()
