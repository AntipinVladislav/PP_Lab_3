import CSV_1
import CSV_2
import CSV_3
import CSV_4
import CSV_5


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class MainWindow(QWidget):
    datapath = ''
    itercat = CSV_5.MyIterator(10)
    iterdog = CSV_5.MyIterator(10)
    listcat = list()
    listdog = list()

    def __init__(self):
        super().__init__()

        self.initUI()

    def dataset1(self):
        CSV_1.createCSV1(self.datapath)

    def dataset2(self):
        CSV_2.copy(self.datapath)
        CSV_2.createCSV2(self.datapath)

    def dataset3(self):
        randlist = CSV_3.randNumberNames()
        CSV_3.copyRand(randlist, self.datapath)
        CSV_3.createCSV3(randlist, self.datapath)

    def nextcat(self):
        try:
            with open(f'{self.datapath}.csv', mode="r", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",", lineterminator="\r")
                row = file_reader.__str__
                filename = row[1][1:len(row[1])]
                print(row[1])
                print(filename)

                self.pixmap = QPixmap(f'{filename}')
                print(f'{self.datapath}\\Cats\\{filename}')
                self.label.setPixmap(self.pixmap)
                self.itercat.__next__
        except StopIteration:
            QMessageBox.about('No more cats, you will now go to the main picture')
            self.itercat = CSV_5.MyIterator(10)
            self.pixmap = QPixmap('NECO.png')
            self.label.setPixmap(self.pixmap)

        
    def nextdog(self):
        try:
            with open(f'{self.datapath}.csv', mode="r", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",", lineterminator="\r")
                for row in file_reader:
                    filename = row[int(self.iterdog.counter)+1000][row[1].rfind('\\')+1:len(row[1])]
                    break
            self.pixmap = QPixmap(f'{self.datapath}/{filename}')
            self.label.setPixmap(self.pixmap)
            self.itercat.__next__
        except StopIteration:
            QMessageBox.about('No more dogs, you will now go to the main picture')
            self.itercat = CSV_5.MyIterator(10)
            self.pixmap = QPixmap('NECO.png')
            self.label.setPixmap(self.pixmap)

    

    def initUI(self):
        self.datapath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        with open(f'{self.datapath}.csv', mode="r", encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",", lineterminator="\r")
                for row in file_reader:
                    self.listcat.append(row[1])



        qbtn1 = QPushButton('Dataset', self)
        qbtn1.move(20, 320)
        qbtn1.clicked.connect(self.dataset1)

        qbtn2 = QPushButton('Dataset with class_names', self)
        qbtn2.move(20, 345)
        qbtn2.clicked.connect(self.dataset2)

        qbtn3 = QPushButton('Dataset with random numbers', self)
        qbtn3.move(20, 370)
        qbtn3.clicked.connect(self.dataset3)

        qbtn4 = QPushButton('Next cat', self)
        qbtn4.move(260, 320)
        qbtn4.clicked.connect(self.nextcat)

        qbtn5 = QPushButton('Next dog', self)
        qbtn5.move(260, 345)
        qbtn5.clicked.connect(self.nextdog)

        self.label = QLabel(self)
        self.pixmap = QPixmap('NECO.png')

        self.label.setPixmap(self.pixmap)
        self.label.move(50, 20)
        self.label.setScaledContents(True)
        self.label.resize(300, 275)

        print('New neco')
        self.pixmap = QPixmap('NECO2.jpg')
        self.label.setPixmap(self.pixmap)

        self.setGeometry(200, 200, 400, 400)
        self.move(800, 300)
        self.setWindowTitle('Cats and Dogs')
        self.setWindowIcon(QIcon('NECO.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
