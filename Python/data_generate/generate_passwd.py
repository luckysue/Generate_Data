#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author jinqinghua@gmail.com
# @version 2012-11-07

import string
from os import urandom
from random import choice

''''' 
Python自带常量(本例中改用这个，不用手工定义了) 
string.digits          #十进制数字：0123456789 
string.octdigits       #八进制数字：01234567 
string.hexdigits       #十六进制数字：0123456789abcdefABCDEF 
string.ascii_lowercase #小写字母(ASCII)：abcdefghijklmnopqrstuvwxyz 
string.ascii_uppercase #大写字母(ASCII)：ABCDEFGHIJKLMNOPQRSTUVWXYZ 
string.ascii_letters   #字母：(ASCII)abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 
string.punctuation     #标点符号：!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 

以下的不用，有locale问题 
string.lowercase       #abcdefghijklmnopqrstuvwxyz 
string.uppercase       #ABCDEFGHIJKLMNOPQRSTUVWXYZ 
string.letters         #ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 

以下的不能用 
string.whitespace      #On most systems this includes the characters space, tab, linefeed, return, formfeed, and vertical tab. 
string.printable       #digits, letters, punctuation, and whitespace 
'''

# 请在此设置您要生成的密码需求
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


def print_string_constants():
    '''''Test Case'''
    print(string.digits)
    print(string.octdigits)
    print(string.hexdigits)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.ascii_letters)
    print(string.punctuation)
    print(string.lowercase)
    print(string.uppercase)
    print(string.letters)
    print(string.printable + "ooo")
    print(string.whitespace)

    print('\n\n')

if __name__ == '__main__':
    # print_string_constants()
    for i in range(0, passwd_count):
        print(generate_passwd())

    print("\ndone...python is great!")
