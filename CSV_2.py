import csv
import os
import shutil
from pathlib import Path


def createCSV2(datapath) -> None:
    """Does the same as createCSV() from CSV_1.py(fills csv file with abs, rel paths and classtag of a picture)
    but in this one the name of the file is class_number.jpg because it changes in def copy()
    """

    with open("dataset_with_classes.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")

        classtag = "Cat"

        for i in range(1000):

            p1 = os.path.abspath(
                f'{datapath}_with_classes/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(
                f'{datapath}_with_classes/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])

        classtag = "Dog"

        for i in range(1000):

            p1 = os.path.abspath(
                f'{datapath}_with_classes/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(
                f'{datapath}_with_classes/{classtag.lower()}_{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])


def copy(datapath):
    """Creates a copy of a file from "Cats" or "Dogs" folder and copies them to just /dataset/
    also changes the names of file from "number.jpg" to "class_number.jpg"
    """
    classtag = 'Cats'
    Path(f'{datapath}_with_classes/Cats').mkdir(parents=True, exist_ok=True)
    for i in range(1000):
        shutil.copyfile(f'{datapath}/Cats/{str(i).zfill(4)}.jpg',
                        f'{datapath}_with_classes/Cats/{str(classtag).lower()}_{str(i).zfill(4)}.jpg')

    Path(f'{datapath}_with_classes/Dogs').mkdir(parents=True, exist_ok=True)
    classtag = 'Dogs'
    for i in range(1000):
        shutil.copyfile(f'{datapath}/Dogs/{str(i).zfill(4)}.jpg',
                        f'{datapath}_with_classes/Dogs/{str(classtag).lower()}_{str(i).zfill(4)}.jpg')
