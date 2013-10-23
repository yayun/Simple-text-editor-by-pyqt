#coding:utf-8
#!usr/bin/python
import sys,os
from PyQt4 import QtCore,QtGui
import ui
from ui import Ui_MainWindow
class main(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.file_dialog=QtGui.QFileDialog()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.fn=None
        QtCore.QObject.connect(self.ui.action_Save,QtCore.SIGNAL("triggered()"),self.save_file)
        QtCore.QObject.connect(self.ui.actionNew,QtCore.SIGNAL("triggered()"),self.new_file)
        QtCore.QObject.connect(self.ui.actionOpen,QtCore.SIGNAL("triggered()"),self.open_file)
        QtCore.QObject.connect(self.ui.action_Saveas,QtCore.SIGNAL("triggered()"),self.saveas_file)
        QtCore.QObject.connect(self.ui.actionPrint,QtCore.SIGNAL("triggered()"),self.save_file)
        QtCore.QObject.connect(self.ui.actionPrint_Preview,QtCore.SIGNAL("triggered()"),self.save_file)
        QtCore.QObject.connect(self.ui.action_quit,QtCore.SIGNAL("triggered()"),self.quit)
    def save_file(self):
        if self.fn!=None:
            fileobj=open(self.fn,'w')
            fileobj.write(self.ui.textEdit.toPlainText())
            fileobj.close()
        else:
            filename=self.file_dialog.getSaveFileName(self,u"保存文件")
            try:
                fileobj=open(filename,'w')
                fileobj.write(self.ui.textEdit.toPlainText())
                self.fn=filename
                fileobj.close()
            except Exception ,e:
                pass
    def saveas_file(self):
        filename=self.file_dialog.getSaveFileName(self,u"文件另存为")
        fileobj=open(self.fn,'w')
        fileobj.write(self.ui.textEdit.toPlainText())
        fileobj.close()
        self.fn=filename
    def new_file(self):
        pass
    def open_file(self):
        filename=self.file_dialog.getOpenFileName(self,u"打开文件")
        if os.path.isfile(filename):
            text=open(filename,'r').read()
            self.ui.textEdit.setPlainText(text)
            self.fn=filename
    def quit(self):
        sys.exit(0)
    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self,'Waring',"Are you sure to quit?",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
if __name__=="__main__":
        app=QtGui.QApplication(sys.argv)
        myapp=main()
        myapp.show()
        sys.exit(app.exec_())
        
