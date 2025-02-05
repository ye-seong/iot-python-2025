class User:
    name = ''
    id = ''
    password = ''

    def __init__(self, name, id, password):
            self.name = name
            self.id = id
            self.password = password

print('========================파이썬에 오신걸 환영합니다.===========================')
user_list = []
admin_pass = '1234'
admin_value = True
error = 0

def adminMode_Service(service):
    if service == '유저정보':
        for user in user_list:
            print('이름: '+user.name)
            print('아이디: '+user.id)
            print('비밀번호: '+user.password)

        go_back = input('뒤로 가시겠습니까? (Y) > ')

        if go_back == 'Y':
            adminMode()

    elif service == '조회수':
        print('아직 정보가 없습니다.')
        go_back = input('뒤로 가시겠습니까? (Y) > ')

    
def adminMode():
    admin_service = input('유저정보 | 조회수 > ')
    if admin_service == '유저정보' or admin_service == '조회수':
        adminMode_Service(admin_service)
    else:
        print('다시 입력 해주세요.')
        adminMode()


def userMode_Service(service, num):
    if service == '개인정보':
            print(f'이름: {user_list[num].name}')
            print(f'아이디: {user_list[num].id}')
            print(f'비밀번호: {user_list[num].password}')

    elif service == '유저리스트':
        for user in user_list:
            print(user.name)
    
    else:
        print('다시 입력 해주세요.')
        userMode(num)


def userMode(num):
    print('=========================파이썬 홈페이지 입니다.===========================')
    mode = input('개인정보 | 유저리스트 > ')
    userMode_Service(mode, num)


def user_account(mode):
    if mode == '로그인':
        id_input = input('아이디 > ')
        pass_input = input('비밀번호 > ')

        user_num = 0

        if len(user_list) < 1:
            print('유저가 없습니다.')
            
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
            while True:
                name_info = input('이름을 입력하세요. > ')
                id_info = input('아이디를 입력하세요. > ')
                pass_info = input('비밀번호를 입력하세요. > ')

                if(name_info == '' or id_info == '' or pass_info == ''):
                    print('다시 입력 해주세요.')
                else:
                    print('가입이 완료되었습니다')
                    info = User(name_info, id_info, pass_info)
                    user_list.append(info)
                    selectLoginAccout()

    elif mode == '뒤로가기':
        selectLoginAccout()


def selectLoginAccout():
    choice = input('로그인 | 회원가입 > ')
    if choice == '로그인' or choice == '회원가입':
        user_account(choice)
    else:
        print('다시 입력 해주세요.')
        selectLoginAccout()


while True:
    mode = input('접속하실 모드를 입력 해주세요. ( 관리자 | 사용자 ) > ')

    if mode == '관리자':
        if admin_value == False:
            print('비밀번호 3회 오류로 관리자 페이지에 접속 할 수가 없습니다.')
        while admin_value:
            admin_pass_input = input('관리자 비밀번호 > ')
            if admin_pass_input == admin_pass:
                print('관리자 모드에 접속 하셨습니다.')
                adminMode()
            else:
                error += 1
                if error >= 3:
                    print('비밀번호가 3회 틀렸습니다. 이전 페이지로 돌아갑니다')
                    admin_value = False
                    break
                else:
                    print(f'비밀번호가 맞지 않습니다. (오류 {error}회. 3회 오류시 닫힙니다.)')
    elif mode == '사용자':
        selectLoginAccout()
        
    else:
        print('유효하지 않은 페이지 입니다.')
