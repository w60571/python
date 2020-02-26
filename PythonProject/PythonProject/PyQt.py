from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('Show data about weather in Warsaw')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Average temp from 1-10th of July = 18; min temp = 15; max temp = 25')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()


#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindown
#import sys

#class MyWindow(QMainWindow):
   # def _init_(self):
      #  super(MyWindow, self)._init_()
       # self.setGeometry(200,200,300,300)
       # self.setWindowTitle("Weather Application")
       # self.iniUI()

   # def iniUI(self):
      #  self.label = QtWidgets.QLabel(self)
       # self.label.setText("Show data about weather in Warsaw")
        #self.label.move(50,50)

     #   self.b1 = QtWidgets.QPushButton(self)
      #  self.b1.setText("Click")
       # self.b1.clicked.connect(self.clicked)

  #  def clicked(self):
   #     self.label.setText("Average temp from 1-10th of July =18 ")
    #    self.update()

  #  def update(self):
   #     self.label.adjustSize()

 

  #  def window():
   #     app = QApplication(sys.argv)
    #    win = MyWindow()
     #   win.show()
    #    sys.exit(app.exec_())
   # window()








#import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot

#def window():
#   app = QApplication(sys.argv)
#   widget = QWidget()
   
#   button1 = QPushButton(widget)
#   button1.setText("Button1")
#   button1.move(64,32)
#   button1.clicked.connect(button1_clicked)

#   button2 = QPushButton(widget)
#   button2.setText("Button2")
#   button2.move(64,64)
#   button2.clicked.connect(button2_clicked)

#   widget.setGeometry(50,50,320,200)
#   widget.setWindowTitle("PyQt5 Button Click Example")
#   widget.show()
#   sys.exit(app.exec_())


#def button1_clicked():
#   print("Button 1 clicked")

#def button2_clicked():
#   print("Button 2 clicked")   
   
#if __name__ == '__main__':
#   window()

#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#app = QApplication([])
#window = QWidget()
#layout = QVBoxLayout()
#layout.addWidget(QPushButton('Top'))
#layout.addWidget(QPushButton('Bottom'))
#window.setLayout(layout)
#window.show()
#app.exec_()
#import numpy as np
#from PyQt5.QtWidgets import QApplication, QMainWindow, \
#    QPushButton, QVBoxLayout, QWidget

#temp = [25, 21, 16, 18, 15, 20, 18, 15, 17, 19]

#def method_name():
#    return temp.read

#def button_min_pressed():
#    ret, frame = temp.read()
#    print(np.min(frame))

#def button_max_pressed():
#    ret, frame = temp.read()
#    print(np.max(frame))

#app = QApplication([])
#win = QMainWindow()
#central_widget = QWidget()
#button_min = QPushButton('Get Minimum', central_widget)
#button_max = QPushButton('Get Maximum', central_widget)
#button_min.clicked.connect(button_min_pressed)
#button_max.clicked.connect(button_max_pressed)
#layout = QVBoxLayout(central_widget)
#layout.addWidget(button_min)
#layout.addWidget(button_max)
#win.setCentralWidget(central_widget)
#win.show()
#app.exit(app.exec_())
#temp.release()

#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#app = QApplication([])
#window = QWidget()
#layout = QVBoxLayout()
#button_min = layout.addWidget(QPushButton('Min Temp'))
#button_max = layout.addWidget(QPushButton('Max Temp'))
#window.setLayout(layout)
#window.show()
#app.exec_()

#from PyQt5.QtWidgets import *
#app = QApplication([])
#button_min = QPushButton('Click')
#def on_button_min_clicked():
#    alert = QMessageBox()
#    alert.setText('The min temp = 15')
#    alert.exec_()
#button.clicked.connect(on_button_min_clicked)
#button.show()
#app.exec_()
#button_max = QPushButton('Click')


#def on_button_clicked():
#    alert = QMessageBox()
#    alert.setText('The max temp = 25')
#    alert.exec_()
#button.clicked.connect(on_button_max_clicked)
#button.show()
#app.exec_()



#import numpy as np
#from PyQt5.QtWidgets import QApplication, QMainWindow, \
#   QPushButton, QVBoxLayout, QWidget
#app = QApplication([])
#window = QWidget()
#layout = QVBoxLayout()
#button_1 = layout.addWidget(QPushButton('average'))
#button_2 = layout.addWidget(QPushButton('min temp'))
#window.setLayout(layout)
#window.show()
#button = QPushButton('average')
#def on_button_clicked():
#    alert = QMessageBox()
#    alert.setText('The average temperature is 18.4')
#    alert.exec_()
#button.clicked.connect(on_button_clicked)
#button.show()
#button = QPushButton('min temp')
#def on_button_clicked():
#    alert = QMessageBox()
#    alert.setText('The minimum temperature is 15')
#    alert.exec()
#app.exec_()