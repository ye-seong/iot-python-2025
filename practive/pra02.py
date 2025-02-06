class User:
    name = ''
    id = ''
    password = ''


    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

    def SameInfo(self, name, id):
        if self.name and self.id == id:
            print('같은 이름과 아이디가 있습니다. 다시 설정해주세요.')
            return True
        elif self.name == name:
            print('같은 이름이 있습니다. 다시 설정해주세요.')
        elif self.id == id:
            print('같은 아이디가 있습니다. 다시 설정해주세요.')
            return True
        else:
            return False

class Admin:
    admin_pass = '1234'
    admin_value = True
    error = 0

class Post:
    post_title = ''
    post_writer = ''
    post_detail = ''

    def __init__(self,title,writer,detail):
        self.post_title = title
        self.post_writer = writer
        self.post_detail = detail


print('========================파이썬에 오신걸 환영합니다.===========================')
user_list = []
post_list = []

def adminMode_Service(service):
    if service == '유저정보':
        for user in user_list:
            print('====================================================')
            print('이름: '+user.name)
            print('아이디: '+user.id)
            print('비밀번호: '+user.password)
            print('====================================================')

        while True:
            go_back = input('뒤로 가시겠습니까? (Y) > ').upper()

            if go_back == 'Y':
                adminMode()
                break
            else:
                continue

    elif service == '조회수':
        print('아직 정보가 없습니다.')
        
        while True:
            go_back = input('뒤로 가시겠습니까? (Y) > ').upper()

            if go_back == 'Y':
                adminMode()
                break
            else:
                continue

    
def adminMode():
    admin_service = input('유저정보 | 조회수 | 뒤로가기 > ')
    if admin_service == '유저정보' or admin_service == '조회수':
        adminMode_Service(admin_service)
    elif admin_service == '뒤로가기':
        main()
    else:
        print('다시 입력 해주세요.')
        adminMode()

def addPost(user, num):
    title = input('게시물 제목 : ')
    writer = user.name
    detail = input('내용 : ')

    save = input('저장하시려면 save를 입력해주세요. 원하지 않을시 엔터를 쳐주세요. : ')
    if save == 'save':
        post_info = Post(title,writer,detail)
        post_list.append(post_info)
        userMode_Service('자유게시판', num)
    else:
        userMode_Service('자유게시판', num)
        

def showPost(num):
    curr_post = post_list[num]
    title = curr_post.post_title
    writer = curr_post.post_writer
    detail = curr_post.post_detail

    print(f'제목 : {title}')
    print(f'글쓴이 : {writer}')
    print(f'내용 : {detail}')
    


def userMode_Service(service, num):
    curr_user = user_list[num]

    if service == '개인정보':
            print(f'이름: {curr_user.name}')
            print(f'아이디: {curr_user.id}')
            print(f'비밀번호: {curr_user.password}')
            while True:
                go_back = input('뒤로 가시겠습니까? (Y) > ').upper()
                if go_back == 'Y':
                    userMode(num)
                    break
                else:
                    continue

    elif service == '유저리스트':
        for user in user_list:
            print(user.name)
        while True:
                go_back = input('뒤로 가시겠습니까? (Y) > ').upper()
                if go_back == 'Y':
                    userMode(num)
                    break
                else:
                    continue

    elif service == '자유게시판':
        number = 0
        for post in post_list:
            number += 1
            print(f'[{number}] {post.post_title}')
        work = input('열람을 원하는 게시물 번호를 입력하세요. 게시물 추가를 원할시 0을 입력해주세요. > ')
        if int(work) == 0:
            addPost(curr_user,num)
        else:
            showPost(int(work)-1)

    elif service == '탈퇴':
        while True:
                answer = input('정말로 탈퇴 하시겠습니까? (Y) > ').upper()
                if answer == 'Y':
                    del(user_list[num])
                    print('탈퇴 되었습니다.')
                    selectLoginAccout()
                    break
                else:
                    print('탈퇴가 취소 되었습니다.')
                    userMode(num)
                    break
            
    elif service == '뒤로가기':
        selectLoginAccout()
    
    else:
        print('다시 입력 해주세요.')
        userMode(num)


def userMode(num):
    print('=========================파이썬 홈페이지 입니다.===========================')
    mode = input('개인정보 | 유저리스트 | 자유게시판 | 탈퇴 | 뒤로가기 > ')
    userMode_Service(mode, num)


def user_account(mode):

    go_back = input('뒤로 가시겠습니까? (Y) > ').upper()
    if go_back == 'Y':
        selectLoginAccout()
    
    if mode == '로그인':
        print('=========================로그인 페이지 입니다.===========================')
        id_input = input('아이디 > ')
        pass_input = input('비밀번호 > ')

        user_num = 0

        for user in user_list:
            if user.id == id_input and user.password == pass_input:
                print(user.name+'님. 환영합니다.')
                userMode(user_num)
            else:
                user_num += 1
                if user_num == len(user_list):
                    print('아이디 및 비밀번호를 다시 확인해주세요.')
                    user_account('로그인')

    elif mode == '회원가입':
        print('=========================회원가입 페이지 입니다.===========================')
        check = False
        while True:
            name_info = input('이름을 입력하세요. > ')
            id_info = input('아이디를 입력하세요. > ')
            pass_info = input('비밀번호를 입력하세요. > ')

            for user in user_list:
                test = User(user.name, user.id, user.password)
                check = test.SameInfo(name_info, id_info)
                if check:
                    user_account('회원가입')

            if name_info == '' or id_info == '' or pass_info == '':
                print('다시 입력 해주세요.')
            else:
                if check == False:
                    print('가입이 완료되었습니다')
                    info = User(name_info, id_info, pass_info)
                    user_list.append(info)
                    selectLoginAccout()

    elif mode == '뒤로가기':
        selectLoginAccout()


def selectLoginAccout():
    choice = input('로그인 | 회원가입 | 뒤로가기 > ')
    if choice == '로그인' or choice == '회원가입':
        user_account(choice)

    elif choice == '뒤로가기':
        main()

    else:
        print('다시 입력 해주세요.')
        selectLoginAccout()

def main():
    while True:
        mode = input('접속하실 모드를 입력 해주세요. ( 관리자 | 사용자 ) > ')
        if mode == '관리자':
            if Admin.admin_value == False:
                print('비밀번호 3회 오류로 관리자 페이지에 접속 할 수가 없습니다.')
            while Admin.admin_value:
                go_back = input('뒤로 가시겠습니까? (Y) > ').upper()
                if go_back == 'Y':
                    main()
                admin_pass_input = input('관리자 비밀번호 > ')
                if admin_pass_input == Admin.admin_pass:
                    print('관리자 모드에 접속 하셨습니다.')
                    adminMode()
                else:
                    Admin.error += 1
                    if Admin.error >= 3:
                        print('비밀번호가 3회 틀렸습니다. 이전 페이지로 돌아갑니다')
                        Admin.admin_value = False
                        break
                    else:
                        print(f'비밀번호가 맞지 않습니다. (오류 {Admin.error}회. 3회 오류시 닫힙니다.)')
        elif mode == '사용자':
            selectLoginAccout()
            
        else:
            print('유효하지 않은 페이지 입니다.')

main()
