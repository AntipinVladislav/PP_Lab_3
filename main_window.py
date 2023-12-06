import CSV_1
import CSV_2
import CSV_3
import CSV_4
import CSV_5


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
            "Are you sure to DIE?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def initUI(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        qbtn = QPushButton('DIE', self)
        qbtn.setStyleSheet("background:yellow")
        qbtn.clicked.connect(self.closeEvent)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(160, 320)

        qbtn1 = QPushButton('Dataset with class_names', self)
        qbtn1.move(50, 320)
        qbtn1 = QPushButton('Dataset with random numbers', self)
        qbtn1.move(50, 370)
        qbtn2 = QPushButton('CAT', self)
        qbtn2.move(260, 320)


        self.setGeometry(200, 200, 400, 400)
        self.move(800, 300)
        self.setWindowTitle('Cats and Dogs')
        self.setWindowIcon(QIcon('NECO.png'))

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())