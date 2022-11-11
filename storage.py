def create_user(d,b):
    c = d + ':' + b
    a = open('nickname', 'a')
    h = a.write(c + '\n')
    a.close()