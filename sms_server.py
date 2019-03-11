#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/3/11 0011'

"""
from flask import Flask,jsonify,request

app =Flask(__name__)

@app.route('/login/',methods=['GET','POST'])
def login():
    user_info = request.json
    user_email =user_info.get('user_email')
    user_pwd = user_info.get('user_pwd')
    # 查询数据库是否有用户，没有用户返回
    # return jsonify({"message":"你还没有注册，是否进行注册"})
    if user_email=='admin@qq.com' and user_pwd =='admin':

        return jsonify({'stats':201,"message":"欢迎"}),201
    else:
        return jsonify({"stats":1001,"message":'用户名或密码错误！'}),403
if __name__ == '__main__':
    app.run()