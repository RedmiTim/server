def create_user(id, name):
    fullname = name + ':' + id
    file = open('nickname', 'a')
    enter_file = file.write(fullname + '\n')
    file.close()
