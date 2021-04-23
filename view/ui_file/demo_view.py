from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)     # x=200; y=200; w=300; h=300
        self.setWindowTitle("Demo Version")      # set windows title
        self.initUI()
        
    def initUI(self):
        # Label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My Fisrt label!")
        self.label.move(50, 50)                  # x=50, y=50
        
        # Button
        self.b1 = QtWidgets.QPushButton(self)    # make button instance
        self.b1.setText("Click Me!")             # set button label
        self.b1.clicked.connect(self.clicked)    # set button click event
        
    def clicked(self):
        self.label.setText("You Just Click Me!")
        self.update()
        
    def update(self):
        self.label.adjustSize()


def window():
    # Main Windows
    app = QApplication(sys.argv)
    win = MyWindow()                     # make windows instance
    win.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    window()