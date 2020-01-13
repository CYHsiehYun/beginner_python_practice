username = input('id: ')
password = input('password: ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('sucess')
else:
    print('try agnin')