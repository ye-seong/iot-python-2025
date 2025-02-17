from tkinter import * 
from tkinter.messagebox import *
import Homepage_code as w
import tkinter as tk

class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('홈페이지')
        self.geometry('1000x700')

        # 프레임 미리 생성
        self.mainF = tk.Frame(self)
        self.adminF = tk.Frame(self)
        self.userF = tk.Frame(self)
        self.adminmodeF = tk.Frame(self)
        
        # 메인화면 출력
        
        self.initWindow()

        # 관리자화면 위젯
        self.adminLabel = Label(self.adminF, text="관리자 비밀번호를 입력하세요.")
        self.adminEntry = Entry(self)
        self.adminBtn = Button(self.adminF, text="로그인", command=self.AdminLogin)

        # 사용자화면 위젯
        self.userLabel = Label(self.userF, text="사용자 화면 입니다.")
        self.userBtn1 = Button(self.userF, text="회원가입", command=self.show_mainF)
        self.userBtn2 = Button(self.userF, text="로그인", command=self.UserLogin)

        # 회원가입화면 위젯
        self.accLabel = Label(self.userF, text="회원가입 화면 입니다.")
        self.accName = Entry(self)
        self.accId = Entry(self)
        self.accPass = Entry(self)
        self.accBtn = Button(self.userF, text="회원가입", command=self.UserLogin)

        # 로그인화면 위젯

        



        
    def initWindow(self):
        self.mainF.pack()
        Label(self.mainF, text="모드를 선택하세요.").pack(pady=20)
        Button(self.mainF, text="관리자", command=self.show_adminF).pack()
        Button(self.mainF, text="사용자", command=self.show_userF).pack()

    def AdminLogin(self):
        password = self.adminEntry.get()
        if w.AdminPass(password):
            pass
        else:
            if w.h.Admin.admin_value:
                showerror('위젯', f'비밀번호를 다시 입력해주세요. ({w.h.Admin.error_num}회 오류)') 
            else:
                showerror('위젯', f'비밀번호 3회 오류로 접속하실 수 없습니다.')             

    def UserLogin(self):
        pass


    # pack

    def pack_adminF(self):
        self.adminLabel.pack(pady=20)
        self.adminEntry.pack()
        self.adminBtn.pack()
        
    def pack_userF(self):
        self.userLabel.pack(pady=20)
        self.userBtn1.pack()
        self.userBtn2.pack()

    def show_mainF(self):
        self.adminF.pack_forget()
        self.userF.pack_forget()
        self.mainF.pack()

    # show Frame

    def show_adminF(self):
        self.mainF.pack_forget()
        self.adminF.pack()
        self.pack_adminF()

    def show_userF(self):
        self.mainF.pack_forget()
        self.userF.pack()
        self.pack_userF()

    def show_adminmodeF(self, password):
        self.adminF.pack_forget()
        self.adminmodeF.pack()

if __name__=="__main__":
    homepage = Homepage()
    homepage.mainloop()


