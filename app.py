#!/usr/bin/env python3
from flask import Flask,render_template
import os,json
app = Flask(__name__)
app.config['TEMPLATES_AUTO_LOAD']=True
@app.route('/')
def index():
    # 显示文章名称的列表：files目下下所有json 文件中的title 信息列表
    files = os.listdir('/home/shiyanlou/files')
    for f in files:
        file_title = []
        with open('/home/shiyanlou/files/'+f,'r')as file:
            file_dic = json.loads(file.read())
            file_title.append(file_dic['title'])
    return render_template('index.html',title=title)
    

'''
@app.route('/files/<filename>')
def file(filename):
    #读取并显示filename.json中的文章内容
    #例如 filename = 'helloshiyanlou' 的时候显示helloshiyanlou.json中的内容
    #如果 filename 不存在，则显示包含字符串'shiyanlou 404' 404 错误页面
    pass
'''
