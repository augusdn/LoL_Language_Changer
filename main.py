import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\Riot Games\League of Legends kr')

        if fname[0]:
            #f = open(fname[0], 'r')
            self.textEdit.setText(fname[0])

            #with f:
            #    data = f.read()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())