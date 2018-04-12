#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: get_base_parms.py
@time: 17-4-13 下午12:18
"""
from lib.MySQL import ConnMysql
from config.get_token import get_token
import random


def get_user_agent(agent):

     chrome = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
     firefox  = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
     webkit = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
     if agent == 'chrome':
         return chrome
     elif agent == 'firefox':
         return firefox
     elif agent == 'webkit':
         return webkit


if __name__ == '__main__':
    print()
