import sys
import os.path
from main import change_language
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QDesktopWidget
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QComboBox, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.folderPath = 'C:\Riot Games\League of Legends'
        self.server = 'Oceania'

        self.initUI()

    def initUI(self):
        yaml_path = self.folderPath + '/system.yaml'
        if os.path.isfile(yaml_path):
            self.folder_check = QLabel('League of Legends Folder Found', self)
            self.folder_path_lbl = QLabel(self.folderPath, self)
        else:
            self.folder_check = QLabel('League of Legends Folder Not Found', self)

        cb = QComboBox(self)
        cb.addItem('Brazil')
        cb.addItem('EU Nordic and East')
        cb.addItem('EU West')
        cb.addItem('Japan')
        cb.addItem('Latin America North')
        cb.addItem('Latin America South')
        cb.addItem('North America')
        cb.addItem('Oceania')
        cb.addItem('Russia')
        cb.addItem('Turkey')

        cb.activated[str].connect(self.server_chosen)

        fileBtn = QPushButton('Open')
        patchBtn = QPushButton('Patch')

        h0box = QHBoxLayout()
        h0box.addStretch(1)
        h0box.addWidget(self.folder_check)
        h0box.addStretch(1)

        h00box = QHBoxLayout()
        h00box.addStretch(1)
        h00box.addWidget(self.folder_path_lbl)
        h00box.addStretch(1)

        h1box = QHBoxLayout()
        h1box.addStretch(1)
        h1box.addWidget(cb)
        h1box.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(fileBtn)
        hbox.addWidget(patchBtn)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(h0box)
        vbox.addLayout(h00box)
        vbox.addLayout(h1box)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        fileBtn.clicked.connect(self.open_dir)
        patchBtn.clicked.connect(self.patch_language)

        self.setWindowTitle('League of Legends Language Patch')
        self.setGeometry(300, 300, 400, 150)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_dir(self):
        self.folderPath = str(QFileDialog.getExistingDirectory(self, "Select League Directory", 'C:\Riot Games\League of Legends'))
        if self.folderPath:
            league_path = self.folderPath + '/system.yaml'
            if os.path.isfile(league_path):
                self.folder_success()
            else:
                self.folder_error()

    def patch_language(self):
        if self.folderPath:
            league_path = self.folderPath + '/system.yaml'
            if os.path.isfile(league_path):
                change_language(self.folderPath, self.server)
                self.update_done()
            else:
                self.folder_error()

    def server_chosen(self, text):
        QMessageBox.about(self, "Server", "Server will be " + text)
        self.server = text

    def update_done(self):
        QMessageBox.about(self, "Patch", "Patch Complete")

    def folder_success(self):
        QMessageBox.about(self, "Success", 'League of Legends folder found')
        self.folder_check.setText('League of Legends folder found')
        self.folder_path_lbl.setText(self.folderPath)

    def folder_error(self):
        QMessageBox.about(self, "Error", 'League of Legends folder not found')
        self.folder_check.setText('League of Legends folder not found')
        self.folder_path_lbl.setText('Folder Not Found')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
