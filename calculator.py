from PyQt4 import QtGui,QtCore
import sys
import sympy
class Main_Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self) 
        self.initUI()
        self.content=""
    def initUI(self):
        All_Item=['','(',')','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
        Grid=QtGui.QGridLayout() #The QGridLayout class lays out widgets in a grid.
        j = 0
        pos = [(0,1),(0,2),(0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]
        for i in All_Item:
            self.button = QtGui.QPushButton(i)
            self.clear_button = QtGui.QPushButton("clear")            
            self.Text=QtGui.QTextEdit(self)            
            Grid.addWidget(self.clear_button, 0, 1)
            Grid.addWidget(self.button, pos[j][0], pos[j][1])
            #The arguments are the widget, the row and the column number.
            j = j + 1
            self.button.clicked.connect(self.clicked)
            self.clear_button.clicked.connect(self.clear)
        self.setLayout(Grid)
        self.show()
    def clicked(self):
        self.content=self.content + self.sender().text()
        self.Text.setText(self.content)
        if "=" in self.content:
            try:
                result=str(self.content[:-1]) #self.content.split("=",1)
                self.Text.setPlainText(str(sympy.sympify(result)))
                #eval(result)
            except ValueError:
                reply=QtGui.QMessageBox.question(self,'Waring',"Syntax error,Please re-enter",
                QtGui.QMessageBox.Yes)
                if reply==QtGui.QMessageBox.Yes:
                     self.Text.setPlainText("")
            finally:
                self.content=""
    def clear(self):
        self.Text.setPlainText("")
def main():
    app=QtGui.QApplication(sys.argv)
    window=Main_Window()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()
    
