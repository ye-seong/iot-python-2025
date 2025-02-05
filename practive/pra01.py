print('=============파이썬에 오신걸 환영합니다.==============')
user_list = []
admin_pass = '1234'

while True:
    choice = input('계정이 있으시다면 로그인, 없으시다면 회원가입을 입력해주세요. > ')

    if choice == '회원가입':
        info = {'name': '', 'id': '', 'password': ''}

        print('====================회원가입====================')

        while info['name'] == '' or info['id'] == '' or info['password'] == '':

            info['name'] = input('이름을 입력하세요. > ')
            info['id'] = input('아이디를 입력하세요. > ')
            info['password'] = input('비밀번호를 입력하세요. > ')

            if(info['name'] == '' or info['id'] == '' or info['password'] == ''):
                print('다시 입력하세요.')
            else:
                print('가입이 완료되었습니다')
                user_list.append(info)
                break
        continue

    elif choice == '로그인':
        print('=====================로그인=====================')

        while True:
            id_input = input('아이디 > ')
            pass_input = input('비밀번호 > ')

            user_num = 0

            for user in user_list:
                if user['id'] == id_input and user['password'] == pass_input:
                    print(user['name']+'님. 환영합니다.')
                else:
                    user_num += 1
                    if user_num == len(user_list):
                        print('아이디 및 비밀번호를 다시 확인해주세요.')
                        continue

            break

    else:
        print('다시 입력하세요.')
        continue

    break

print('==============================파이썬 홈페이지============================')

service = input(' 관리자 | 유저 리스트 > ')

admin_value = True

error = 0

if service == '관리자':
    if admin_value == False:
        print('비밀번호 3회 오류로 관리자 페이지에 접속 할 수가 없습니다.')
    while admin_value:
        admin_pass_input = input('관리자 비밀번호 > ')
        if admin_pass_input == admin_pass:
            print('관리자 페이지 접속 완료.')
            admin_service = input(' 유저 정보 | 조회수 > ')
            if admin_service == '유저 정보':
                for user in user_list:
                    print ('이름: '+user['name'])
                    print ('아이디: '+user['id'])
                    print ('비밀번호: '+user['password'])
            break
        else:
            error += 1
            if error >= 3:
                print('비밀번호가 3회 틀렸습니다. 홈페이지로 돌아갑니다')
                service = input(' 관리자 | 유저 리스트 > ')
                admin_value = False
            else:
                print(f'비밀번호가 맞지 않습니다. (오류 {error}회. 3회 오류시 닫힙니다.)')

if service == "유저 리스트":
    for user in user_list:
        print(user['name']+'\n')

    
    
        

    









        




