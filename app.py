# -*- coding: utf-8 -*-
"""
@Author    : 君莫笑
@Email     : w_petrichor@163.com
@Time      : 2020/7/8/008 17:15
@File      : app.py
@Version   : 1.0
@Desciption: 
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'welcome to my watchlist!'

