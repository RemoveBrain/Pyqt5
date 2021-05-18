import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip,QMainWindow , QAction, qApp ,QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt

class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "계산기"
        self.setWindowTitle(self.title)
        self.left = 100
        self.top = 200
        self.width = 300
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.cal = NewWindow()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        editAction = QAction(QIcon('edit.png'),'Center',self)
        editAction.setStatusTip('go to center')
        editAction.triggered.connect(self.center)


        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)  # 맥에서의 윈도우 메뉴바 세팅이라고 함.
        filemenu = menubar.addMenu('&Edit')
        filemenu.addMenu("window").addAction(editAction)

        sizeAction = QAction(QIcon('save.png'), 'Up', self)
        sizeAction.setStatusTip('resize')
        sizeAction.triggered.connect(self.upsize)

        sm = filemenu.addMenu("resize")
        sm.addAction(sizeAction)

        sizeAction = QAction(QIcon('save.png'), 'Down', self)
        sizeAction.setStatusTip('resize')
        sizeAction.triggered.connect(self.downsize)

        sm.addAction(sizeAction)

        btn = QPushButton('계산기', self)
        btn.setToolTip('누르면 새창이 열립니다.')
        btn.move(150, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.calc)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setWindowIcon(QIcon('web.png'))
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('나의 첫 어플')
        self.move(500, 300)
        self.resize(400, 400)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def upsize(self):
        self.resize(self.width()+100,self.height()+100)

    def downsize(self):
        self.resize(self.width()-100,self.height()-100)

    def calc(self):
        self.cal.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
