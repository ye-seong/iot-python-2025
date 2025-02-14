from tkinter import * 
from tkinter.messagebox import *
import Homepage_code as w

class Homepage(Tk):
    def __init__(self):
        super().__init__()
        self.title('홈페이지')
        self.geometry('1000x700')

        self.frame1 = Tk.frame(self)
        entry = Entry(self)
        Label(entry, text="메인화면").pack(pady=20)
        Button(entry, text="다음화면", command=self.show_frame2).pack()
        entry.pack()

        self.frame2 = Tk.frame(self)
        Label(entry, text="두번째화면").pack(pady=20)
        Button(entry, text="이전화면", command=self.show_frame1).pack()

    def show_frame1(self):
        self.frame2.pack_forget()
        self.frame1.pack()

    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame2.pack()

if __name__=="__main__":
    homepage = Homepage()
    homepage.mainloop()

# def AdminBtnClick():
#     test = w.AdminMode()
#     if test:
#         root.
#         Label(root, text='관리자 비밀번호를 입력하세요.')
#         entry = Entry(root).pack()
#         if entry == '1234':
#             showinfo('접속')
#     else:
#         showinfo('메시지', '비밀번호 3회 오류로 접속하실 수 없습니다.')


# Label(root, text='====================파이썬 홈페이지에 오신 것을 환영합니다!====================').pack()
# admin_button = Button(root, text='관리자', command=AdminBtnClick).pack()
# admin_button = Button(root, text='사용자', command=AdminBtnClick).pack()


# entry = Entry(root)
# entry.pack()


# root.mainloop()