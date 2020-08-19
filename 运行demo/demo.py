#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-08-19 10:26:14
# @Author  : Octan3 (Octan3@qq.com)
# @Link    : http://liyue.site
# @Version : 1.0
# @Function: Demo for picture_to_py

import tkinter as tk  # 使用Tkinter前需要先导入
import os
import base64

from one_gif import img as one   #导入第一张图片的py文件，重命名为one
from two_gif import img as two   #导入第一张图片的py文件，重命名为two

#先把图片弄出来
tmp = open('one.gif', 'wb')        #创建临时的文件, 这里把后缀改成了gif，因为tk只认识gif格式图片
tmp.write(base64.b64decode(one))    ##把这个one图片解码出来，写入文件中去。
tmp.close()  
tmp2 = open('two.gif', 'wb')        #创建临时的文件,这里把后缀改成了gif，因为tk只认识gif格式图片
tmp2.write(base64.b64decode(two))    ##把这个two图片解码出来，写入文件中去。
tmp2.close()  
#到此为止，图片资源已经由py文件中的字符串重新解码写入到了临时图片中，可以直接使用one.png, two.png

# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=200, width=500)
# 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='one.gif')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image_file2 = tk.PhotoImage(file='two.gif')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
image = canvas.create_image(150, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（0,0）坐标处
image2 = canvas.create_image(300, 0, anchor='n',image=image_file2)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处

canvas.pack()
 
# 第5步，主窗口循环显示
window.mainloop()

#删除生成的临时图片
os.remove('one.gif')
os.remove('two.gif')

