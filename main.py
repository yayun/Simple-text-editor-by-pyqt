#coding:utf-8
#!usr/bin/python
import sys,os
from PyQt4 import QtCore,QtGui
import ui
from ui import Ui_MainWindow
class main(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.action_Save,QtCore.SIGNAL("triggered()"),self.save_file)
        QtCore.QObject.connect(self.ui.actionNew,QtCore.SIGNAL("triggered()"),self.save_file)
         QtCore.QObject.connect(self.ui.actionOpen,QtCore.SIGNAL("triggered()"),self.save_file)
         QtCore.QObject.connect(self.ui.actionCut,QtCore.SIGNAL("triggered()"),self.save_file)
         QtCore.QObject.connect(self.ui.actionSaveas,QtCore.SIGNAL("triggered()"),self.save_file)
         QtCore.QObject.connect(self.ui.actionPrint,QtCore.SIGNAL("triggered()"),self.save_file)
         QtCore.QObject.connect(self.ui.actionPrint_Preview,QtCore.SIGNAL("triggered()"),self.save_file)
    def save_file(self):
        
       
        
if __name__=="__main__":
        app=QtGui.QApplication(sys.argv)
        myapp=main()
        myapp.show()
        sys.exit(app.exec_())
        
