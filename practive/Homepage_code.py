import Homepage_module as h

def addToUserDB(items: list):
    f = open('user_db.txt', encoding='utf-8', mode='w')
    for item in items:
        f.write(f'{item.name}|')
        f.write(f'{item.id}|')
        f.write(f'{item.password}\n')

    f.close()

def addToPostDB(items: list):
    f = open('opst_db.txt', encoding='utf-8', mode='w')
    for item in items:
        f.write(f'{item.post_writer}|')
        f.write(f'{item.post_title}|')
        f.write(f'{item.post_detail}|')
        f.write(f'{item.post_reply}')

    f.close()

def LoadUserFromDB(items: list):
    f = open('user_db.txt', encoding='utf-8', mode='r')
    while True:
        line = f.readline().replay('\n', '')
        if not line: break
        
        lines = line.split('|')
        name = lines[0]
        id = lines[1]
        password = lines[2]

        user = h.User(name, id, password)
        h.user_list.append(user)
    
    f.close()

def LoadPostFromDB(items: list):
    f = open('post_db.txt', encoding='utf-8', mode='r')
    while True:
        line = f.readline().replace('\n', '')
        if not line: break
        
        lines = line.split('|')
        writer = lines[0]
        title = lines[1]
        detail = lines[2]
        reply = lines[3]

        post = h.Post(writer, title, detail, reply)
        h.post_list.append(post)
    f.close()

def AdminMode():
    if h.Admin.admin_value == False:
        print('접속불가')
        return False
    else:
        print('비밀번호 입력')
        return True
        
def AdminPass(password):
    if password == h.Admin.admin_pass:
        return True
    else:
        return False