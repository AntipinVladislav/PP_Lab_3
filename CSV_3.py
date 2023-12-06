import csv
import os
import shutil
import random

from typing import List


def createCSV3(randlist: List[int]) -> None:
    """creates csv file using randomly generated list from def randNumberNames()
    the algorythm is the same as before but name of the file is chenged to
    "number.jpg" (it was "0001.jpg" and now becomes "just 1.jpg")

    Args:
        randlist (List[int]): list of integer
    """
    with open("dataset3.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")

        classtag = "Cat"
        for i in range(1000):

            p1 = os.path.abspath(f'dataset/{randlist[i]}.jpg')

            p2 = os.path.relpath(f'dataset/{randlist[i]}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])

        classtag = "Dog"
        for i in range(1000):

            p1 = os.path.abspath(f'dataset/{randlist[i+1000]}.jpg')

            p2 = os.path.relpath(f'dataset/{randlist[i+1000]}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])


def copyRand(randlist: List[int]) -> None:
    """Copies pictures from dataset/Cats and dataset/Dogs to dataset/ and changes 
    file names to list elements, which are randomised in def randNumberNames()

    Args:
        randlist (List[int]): List of integer
    """
    classtag = 'Cats'
    for i in range(1000):
        shutil.copyfile(
            f'dataset/Cats/{str(i).zfill(4)}.jpg', f'dataset/{randlist[i]}.jpg')
    classtag = 'Dogs'
    for i in range(1000):
        shutil.copyfile(
            f'dataset/Dogs/{str(i).zfill(4)}.jpg', f'dataset/{randlist[i+1000]}.jpg')


def randNumberNames() -> List[int]:
    """Creates list of 10000 elements from 1 to 10000
    Then shuffles it to create randomised list

    Returns:
        List[int]: List of integer
    """
    randlist = list(range(10000))
    random.shuffle(randlist)
    return randlist


if __name__ == "__main__":

    randlist = randNumberNames()
    copyRand(randlist)
    createCSV3(randlist)
