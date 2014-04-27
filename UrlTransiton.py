# -*- coding: utf-8 -*-
#--------------------------
#   python 2.7
#   author:loster
#   version:0.1
#   description:将下载地址转换成迅雷和qq旋风的下载地址
#--------------------------
import re
import base64
from PyQt4 import QtGui,QtCore
import os
import sys

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.linklabel=QtGui.QLabel('link:',self)
        self.link=QtGui.QLineEdit(self) 
        
        self.thunderlabel=QtGui.QLabel('Thunder:',self)
        self.thunder=QtGui.QLineEdit(self)

        self.qqdllabel=QtGui.QLabel('qqdl',self)
        self.qqdl=QtGui.QLineEdit(self)

        transbutton=QtGui.QPushButton('Transition',self)

        grid=QtGui.QGridLayout()
        grid.addWidget(self.linklabel)
        grid.addWidget(self.link)
        grid.addWidget(self.thunderlabel)
        grid.addWidget(self.thunder)
        grid.addWidget(self.qqdllabel)
        grid.addWidget(self.qqdl)
        grid.addWidget(transbutton)

        self.resize(500,200)
        self.setLayout(grid)
        self.setWindowTitle('Transition  by loster v0.1')

        self.connect(transbutton,QtCore.SIGNAL('clicked()'),Trans)

    def getUrl(self):
        return self.link.text()
    def setThunder(self,url):
        self.thunder.setText(url)
    def setQQDL(self,url):
        self.qqdl.setText(url)
    def setError(self,warning):
        QtGui.QMessageBox.warning( self, "Transition", warning, QtGui.QMessageBox.Yes )
        
def Trans():
    #获得链接
    url=main.getUrl() 
    print 'url:'+url
    if CheckUrl(url):
        main.setThunder(Url2Thunder(url))
        main.setQQDL(Url2QQdl(url))
    else:
        main.setError('Invalid link,Please try again')
    
#判断url是否有效
def CheckUrl(url):
    if re.match('(http|https|ftp|ed2k)://', url):
        return True
    else:
        return False

#转化成迅雷下载地址
def Url2Thunder(url):
    url='AA'+url+'ZZ'
    url = base64.b64encode(url)  
    url = 'thunder://' + url
    print 'thunder:'+url
    return url

#转换成qq旋风下载地址
def Url2QQdl(url):  
    url = base64.b64encode(url)  
    url = 'qqdl://' + url
    print 'QQDL:'+url
    return url

if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    main=Window()
    main.show()
    sys.exit(app.exec_())
    
