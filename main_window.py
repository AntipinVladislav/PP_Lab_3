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
    """Class is used to describe window properties, 2 iterators for cats and dogs count, lists for properly reading csv file
    Args:
        QWidget (Window): Main window for the programm
    """
    datapath = ''
    itercat = CSV_5.MyIterator(1000)
    iterdog = CSV_5.MyIterator(1000)
    listcat = list()
    listdog = list()

    def __init__(self) -> None:
        """initializes class
        """
        super().__init__()

        self.initUI()

    def dataset1(self) -> None:
        """creates basic csv file
        """
        CSV_1.createCSV1()

    def dataset2(self) -> None:
        """creates new dataset folder with copied files from first one, also renames them slightly
        """
        CSV_2.copy()
        CSV_2.createCSV2()

    def dataset3(self) -> None:
        """creates copies with random numbers and puts them in new csv and folder
        """
        randlist = CSV_3.randNumberNames()
        CSV_3.copyRand(randlist)
        CSV_3.createCSV3(randlist)

    def nextcat(self) -> None:
        """shows new cat image
        """
        try:
            self.pixmap = QPixmap(f'{self.listcat[self.itercat.counter]}')
            print(f'{self.listcat[self.itercat.counter]}')
            self.label.setPixmap(self.pixmap)
            next(self.itercat)

        except StopIteration:
            QMessageBox.information(
                self, 'CAT', 'No more cats, you will now go to the main picture')
            self.itercat = CSV_5.MyIterator(1000)
            self.pixmap = QPixmap('NECO.png')
            self.label.setPixmap(self.pixmap)

    def nextdog(self) -> None:
        """shows new dog image
        """
        try:
            self.pixmap = QPixmap(f'{self.listdog[self.iterdog.counter]}')
            print(f'{self.listdog[self.iterdog.counter]}')
            self.label.setPixmap(self.pixmap)
            next(self.iterdog)
        except StopIteration:
            QMessageBox.information(
                self, 'DOG', 'No more dogs, you will now go to the main picture')
            self.iterdog = CSV_5.MyIterator(1000)
            self.pixmap = QPixmap('NECO.png')
            self.label.setPixmap(self.pixmap)

    def initUI(self) -> None:
        """creates the GUI
        """
        self.datapath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        with open(f'{self.datapath}.csv', mode="r", encoding='utf-8') as r_file:
            count = 0
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                if count < 1000:
                    self.listcat.append(row[1])
                    count += 1
                else:
                    self.listdog.append(row[1])
                    count += 1

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

        self.setGeometry(200, 200, 400, 400)
        self.move(800, 300)
        self.setWindowTitle('Cats and Dogs')
        self.setWindowIcon(QIcon('NECO.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
