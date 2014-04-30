# -*- coding: utf-8 -*-
#--------------------------
#   python 2.7
#   author:loster
#   version:0.2
#   description:将下载地址转换成迅雷和qq旋风的下载地址
#--------------------------
import re
import base64
from PyQt4 import QtGui,QtCore
import os
import sys
import win32clipboard
import win32con


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.linklabel=QtGui.QLabel('link:',self)
        self.link=QtGui.QLineEdit(self) 
        
        self.thunderlabel=QtGui.QLabel('Thunder:',self)
        self.thunder=QtGui.QLineEdit(self)
        self.thundercopy=QtGui.QPushButton('tcopy',self)
        
        self.qqdllabel=QtGui.QLabel('qqdl',self)
        self.qqdl=QtGui.QLineEdit(self)
        self.qqdlcopy=QtGui.QPushButton('qcopy',self)

        transbutton=QtGui.QPushButton('Transition',self)
        clearbutton=QtGui.QPushButton('Clear All',self)
         
        grid=QtGui.QGridLayout()
        grid.addWidget(self.linklabel,0,0)
        grid.addWidget(self.link,1,0,1,3)
        
        grid.addWidget(self.thunderlabel,2,0)
        grid.addWidget(self.thunder,3,0,1,3)
        grid.addWidget(self.thundercopy,3,4)
         
        grid.addWidget(self.qqdllabel,4,0)
        grid.addWidget(self.qqdl,5,0,1,3)
        grid.addWidget(self.qqdlcopy,5,4)
         
        grid.addWidget(transbutton,6,0)
        grid.addWidget(clearbutton,6,2)
        
        self.resize(500,200)
        self.setLayout(grid)
        self.setWindowTitle('Transition  by loster v0.1')
        
        self.connect(self.thundercopy,QtCore.SIGNAL('clicked()'),CopyThunder)       
        self.connect(self.qqdlcopy,QtCore.SIGNAL('clicked()'),CopyQQDL)
        self.connect(transbutton,QtCore.SIGNAL('clicked()'),Trans)
        self.connect(clearbutton,QtCore.SIGNAL('clicked()'),ClearAll)
        
    def getUrl(self):
        return self.link.text()
    def setUrl(self,url):
        return self.link.setText(url)
    def setThunder(self,url):
        self.thunder.setText(url)
    def getThunder(self):
        return self.thunder.text()
   
    def setQQDL(self,url):
        self.qqdl.setText(url)
    def getQQDL(self):
        return self.qqdl.text()
    def setWarning(self,warning):
        QtGui.QMessageBox.warning( self, "Transition", warning, QtGui.QMessageBox.Yes )
       
def CopyThunder():
    text=main.getThunder()
    if text=='':
        pass
    else:
        Copy(str(text))
def CopyQQDL():
    text=main.getQQDL()
    if text=='':
        pass
    else:
        Copy(str(text))
#复制到剪切板

def Copy(text):
    #print text
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT,text)
    win32clipboard.CloseClipboard()
    main.setWarning('the link is on your clipboard now')
    
def Trans():
    #获得链接
    url=main.getUrl() 
    print 'url:'+url
    if CheckUrl(url):
        main.setThunder(Url2Thunder(url))
        main.setQQDL(Url2QQdl(url))
    else:
        main.setWarning('Invalid link,Please try again')
def ClearAll():
    main.setUrl('')
    main.setThunder('')
    main.setQQDL('')
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
    
