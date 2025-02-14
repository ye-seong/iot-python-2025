from tkinter import * 
from tkinter.messagebox import *
import Homepage_code as w
import tkinter as tk

class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('홈페이지')
        self.geometry('1000x700')

        self.mainF = tk.Frame(self)
        Label(self.mainF, text="모드를 선택하세요.").pack(pady=20)
        Button(self.mainF, text="관리자", command=self.show_adminF).pack()
        Button(self.mainF, text="사용자", command=self.show_userF).pack()
        self.mainF.pack()

        self.adminF = tk.Frame(self)
        Label(self.adminF, text="관리자 비밀번호를 입력하세요.").pack(pady=20)
        admin_entry = Entry(self)
        admin_entry.pack()
        Button(self.adminF, text="로그인", command=self.show_adminmodeF(admin_entry.get())).pack()

        self.adminmodeF = tk.Frame(self)
        Label(self.adminmodeF, text="관리자 화면 입니다.").pack(pady=20)
        # Button(self.adminmodeF,text="")
        
        self.userF = tk.Frame(self)
        Label(self.userF, text="사용자 화면 입니다.").pack(pady=20)
        Button(self.userF, text="사용자", command=self.show_mainF).pack()

    def show_mainF(self):
        self.adminF.pack_forget()
        self.mainF.pack()

    def show_adminF(self):
        self.mainF.pack_forget()
        self.adminF.pack()

    def show_userF(self):
        self.mainF.pack_forget()
        self.userF.pack()

    def show_adminmodeF(self, password):
        self.adminF.pack_forget()
        self.adminmodeF.pack()
        # if w.AdminPass(password):
            
        # else:
        #     # showinfo('위젯', '비밀번호가 틀렸습니다!')
        #     pass

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