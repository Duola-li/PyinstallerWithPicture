[博客原文](https://blog.csdn.net/Monster_li57/article/details/80601050)

1. 先把图片放到 **/图片处理** /下，修改Pic2py.py的第11行，写上你要处理的图片的名字。一般来说tkinter要用gif格式的图片。pyqt都行。
	   ![enter description here](https://gitee.com/octan3/images_bed/raw/master/小书匠/1597805364663.png)
2. 运行**Pic2py.py**, 得到对应的py文件，复制到 项目文件架 里面。
	   ![enter description here](https://gitee.com/octan3/images_bed/raw/master/小书匠/1597805458166.png)
3. 在 项目文件中使用，参考demo文件，大体流程是先导入再解码写入文件，还原出图片，然后就能用了。最后用完可以删掉。
	   ![enter description here](https://gitee.com/octan3/images_bed/raw/master/小书匠/1597805541822.png)
4. 再打包，就会自动把相关的py文件打包进去，这样程序就能找到图片了。