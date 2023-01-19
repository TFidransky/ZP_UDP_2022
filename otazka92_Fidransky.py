import csv
from collections import Counter
from itertools import chain
import os

# This program reads a csv file and calculates the most frequent element (modus) in the file.


    # The class EmptyFileException is used to handle the exception when the input file is empty.
class EmptyFileException(Exception):
    def __init__(self, message):
        self.message = message

class MyFileProcessor:
    def __init__(self, input_file):
        self.input_file = input_file

        # Program controls if the file is empty or if it exists at all. If it doesn't exist, it asks the user again, for a different input.
        # The file is first read using the csv library and stored in a list of lists called "data".
        # If the file is not found or is empty, the program raises an exception and exits.
    def open_file(self):
        while True:
            try:
                with open(self.input_file, 'r') as input_file:
                    if os.stat(self.input_file).st_size == 0:
                        raise EmptyFileException("Input file is empty.")
                    reader = csv.reader(input_file)
                    data = [row for row in reader]
                    break
            except FileNotFoundError:
                self.input_file = input("Input file was not found. Please enter the correct file name: ")
            except EmptyFileException as EmptyError:
                print(EmptyError)
                exit(1)
        return data

        # The function modus_calculation takes the data as an input and first flattens the list of lists into a single list using itertools chain.
        # Then it sorts the list using bubble sort algorithm.
            # The Bubble sort is a simple algorithm and is easy to implement.
            # It's not the most efficient algorithm for big datasets, but this program is not really meant for that - and it is fairly efficient for small datasets.
        # It then uses the Counter class from the collections module to count the frequency of each element in the sorted list.
        # It stores the most common element and its frequency in the variables "most_common" and "frequency".
        # Finally, it prints the most common element and its frequency.
    def modus_calculation(self, data):
        data_sorted = chain(*data)
        data_sorted = list(data_sorted)
        for i in range(len(data_sorted)):
            for j in range(len(data_sorted)-1):
                if data_sorted[j] > data_sorted[j+1]:
                    data_sorted[j], data_sorted[j+1] = data_sorted[j+1], data_sorted[j]
        c = Counter(data_sorted)

        most_common, frequency = c.most_common(1)[0]

        print(f"The element that appeared most frequently in the file was: {most_common}.")
        print(f"This element (= modus) appeared {frequency} times in the file.")

    # It asks user for the name of the file. It then goes into MyFileProcessor class and goes through all the functions there. For more thorough explaination, go to individual functions 
def main():
    input_file = input("Type the name of the CSV file you want to know the modus of, for example input.csv: ")
    file_processor = MyFileProcessor(input_file)
    data = file_processor.open_file()
    file_processor.modus_calculation(data)

main()