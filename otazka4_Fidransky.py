import re
import os

class CharFrequencyAnalyzer:
        # Constructor that prompts user for input string.
    def __init__(self):
        self.string = input("Input the sentence of which you want to know the frequency of each character: ")

        # Counts the frequency of each character in the input string and prints the results in descending order (from most frequent to least frequent).
            # If the character didnt appear yet, it will give that character value 1, if it did appear prior to that appearance, it will add 1 to its current value.
            # The program doesn't count special symbols like . , : and simillar. It could be modified so it would count only letters from specific alphabets and/or numbers, 
            # but it would not be as universal, because different alphabets use specific symbols, such as ř or š, that are not universally used and therefore it would be hard to implement a universal counter
        # Lastly, the function returns a list of characters sorted from the most frequent to the least frequent. This list is used in the print function.
    def char_freq(self):
        string = self.string.upper()
        char_freq = {}
        unwanted_chars = ".,:!?_-;%ˇ´<>'(){}[] \" "


        for char in string:
            if char not in unwanted_chars:
                if char not in char_freq:
                    char_freq[char] = 1
                else:
                    char_freq[char] += 1

        char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

        return char_freq

        # This function simply prints the list of characters and their usage in the sentence inputted by user.
    def print_char_freq(self, char_freq):
        for char, freq in char_freq:
            print(f"{char}: {freq}")
      
      # Main function that calls the char_freq function if a valid input string is provided.
    def main(self):
        if self.string.strip() != "":
            char_freq = self.char_freq()
            self.print_char_freq(char_freq)
        else:
            print("No input was recorded, try again.")

  # Create an instance of the CharFrequencyAnalyzer class and call the main function
analyzer = CharFrequencyAnalyzer()
analyzer.main()