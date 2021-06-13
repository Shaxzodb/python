import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 479)
        MainWindow.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color:#010;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color:#000;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:#fff;\n"
"padding:2px;")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-color:#fff;\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color:blue;\n"
"padding:2px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.saqlash(B))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: blue;\n"
"color:#fff;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#fff;\n"
"color:#000;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.qdelete())
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(21, 255, 56);\n"
"color:#fff;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#fff;\n"
"color:#000;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.delete())
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: red;\n"
"color:#fff;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#fff;\n"
"color:#000;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        try:
                with open("pkl","rb") as fail:
                        M=pickle.load(fail)
        except:
                pass
        
        # with open("fail.txt") as faile:
        #         M=faile.read()
              
        try:
                N=json.loads(M)
                N=list(N)
                for i in range(len(N)):
                        self.listWidget.addItem(N[i])
                B=N    
                
        except:
                B=[]
        try:
                if M=="": 
                        self.listWidget.clear()
        except:
                pass
    def saqlash(self,B):
        text=self.lineEdit.text()    
        if text=='':
               pass
        else:
                B.append(text)
                C=json.dumps(B)
                with open("pkl","wb") as file:
                        pickle.dump(C,file)
        # with open("fail.txt","w") as faile: 
        #         faile.write('')
        # with open("fail.txt","a") as faile:  
        #         faile.write(C)
                self.listWidget.addItem(text)
                self.lineEdit.setText("")

    def qdelete(self):
        try:
                with open("pkl","rb") as fail:
                        M=pickle.load(fail)
                # with open("fail.txt") as faile:
                #         M=faile.read()
                N=json.loads(M)
                N=list(N)
                N.pop(self.listWidget.currentRow())
                N=json.dumps(N)
                with open("pkl","wb") as file:
                        pickle.dump(N,file)
                # with open("fail.txt","w") as faile: 
                #         faile.write(N)
                self.listWidget.takeItem(self.listWidget.currentRow())
        except:
                pass
    def delete(self):
       
        with open("pkl","wb") as file:
                pickle.dump("",file)
        self.listWidget.clear()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Saqlash"))
        self.pushButton_3.setText(_translate("MainWindow", "Qatorni Tozalash"))
        self.pushButton_2.setText(_translate("MainWindow", "Tozalash"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
