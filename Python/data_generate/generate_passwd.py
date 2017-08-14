# -*- coding: utf-8 -*-

import string
from os import urandom
from random import choice

# 设置要生成的密码需求
passwd_length = 20  # 密码长度
passwd_count = 100  # 密码个数
passwd_seed = string.digits + string.ascii_letters + string.punctuation  # 密码种子

# passwd_seed = string.digits
# passwd_seed = string.digits + string.ascii_letters

def generate_passwd():
    '''''Function to generate a password'''
    passwd = []
    while (len(passwd) < passwd_length):
        passwd.append(choice(passwd_seed))
    return ''.join(passwd)

if __name__ == '__main__':
    # print_string_constants()
    for i in range(0, passwd_count):
        print(generate_passwd())

    print("done !")
