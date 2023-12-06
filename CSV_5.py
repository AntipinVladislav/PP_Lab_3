import csv


def classElements(classtag: str, dataset: str):
    """Prints relative paths of provided classtag elements from provided dataset
    this time with custom iterator

    Args:
        classtag (str): name of the element class, like 'Cat' or 'Dog'
        dataset (str): the name of csv file from which def reads needed pictures
    """
    my_iter = MyIterator(1000)

    with open(dataset, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")

        for row in file_reader:
            if row[2] == ' ' + classtag:
                print(row[1])
                my_iter.__next__()


class MyIterator:

    def __init__(self, limit: int) -> None:
        """initializes MyIterator

        Args:
            limit (int): limit of limited limitations (how many times iterator can go next)
        """
        self.limit = limit
        self.counter = 0

    def __next__(self) -> None:
        """Increments iterator

        Raises:
            StopIteration: Stops further incrementation of iterator
        """
        if self.counter < self.limit:
            self.counter += 1
        else:
            raise StopIteration


if __name__ == "__main__":

    classtag = str(input())
    dataset = str(input())
    classElements(classtag, dataset)
