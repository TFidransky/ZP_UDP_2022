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

        # Program controls if the file is empty and if it exists at all. If it doesn't exist, it asks the user again, for a different input. 
            # If the file is empty, it will give the user an appropriate error code and then the program will end.
        # The file is first read using the CSV library and then stored in a list of lists 
            # list of lists = each sub-list represents exactly one row (but all columns in that one row) in the file called "data". It returns this list for further usage.
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

        # The function prepare_data takes the list of lists "data" as an input and flattens it into a single list using itertools chain.
        # It returns this one singular list for further usage, specifically for sorting
    def prepare_data(self, data):
        data_sorted = chain(*data)
        data_sorted = list(data_sorted)
        return data_sorted

        # The bubble_sort sorts the list using bubble sort algorithm.
            # The Bubble sort is a simple algorithm and is quite easy to implement.
            # It's not the most efficient algorithm for big datasets, but this program is not really meant for that - and it's fairly efficient for small datasets.
        # It then returns this list so the modus can be found in the next function
    def bubble_sort(self, data_sorted):
        for i in range(len(data_sorted)):
            already_sorted = True
            for j in range(len(data_sorted)-1):
                if data_sorted[j] > data_sorted[j+1]:
                    data_sorted[j], data_sorted[j+1] = data_sorted[j+1], data_sorted[j]
                    already_sorted = False
            if already_sorted:
                break
        return data_sorted

        # This function takes the now sorted data as input and uses the Counter class to count the frequency of each element in that sorted list.
        # It then stores the most common element and its frequency in the variables "most_common" and "frequency" respectively and returns them as a tuple.
    def modus_finder(self, data_sorted):
        c = Counter(data_sorted)
        most_common, frequency = c.most_common(1)[0]
        return most_common, frequency

        # Finally, this part takes the tuple of most frequent element and its frequency and prints it out to the terminal.
    def print_modus(self, most_common, frequency):
        print(f"The element that appeared most frequently in the file was: {most_common}.")
        print(f"This element (= modus) appeared {frequency} times in the file.")

    # After program startup, the program prompts the user for the name of the CSV file and create an instance of MyFileProcessor class with the 
    # input file name and proceeds to commit the functions in that class
def main():
    input_file = input("Type the name of the CSV file you want to know the modus of, for example input.csv: ")
    file_processor = MyFileProcessor(input_file)
    data = file_processor.open_file()
    data_sorted = file_processor.prepare_data(data)
    data_sorted = file_processor.bubble_sort(data_sorted)
    most_common, frequency = file_processor.modus_finder(data_sorted)
    file_processor.print_modus(most_common, frequency)

main()