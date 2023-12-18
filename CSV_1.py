import csv
import os


def createCSV1(datapath) -> None:
    """Creates csv file and goes in folder dataset/Cats and dataset/Dogs
    Rows of csv are created from absolute path of picture, relative and its classtag
    which is the name of the folder
    """
    with open("dataset.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")

        classtag = "Cat"
        for i in range(1000):

            p1 = os.path.abspath(
                f'{datapath}/{classtag}s/{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(
                f'{datapath}/{classtag}s/{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])

        classtag = "Dog"
        for i in range(1000):

            p1 = os.path.abspath(
                f'{datapath}/{classtag}s/{str(i).zfill(4)}.jpg')

            p2 = os.path.relpath(
                f'{datapath}/{classtag}s/{str(i).zfill(4)}.jpg')

            file_writer.writerow([f"{p1}", f" {p2}", f" {classtag}"])


def main(datapath):
    createCSV1(datapath)


if __name__ == "__main__":
    createCSV1()
