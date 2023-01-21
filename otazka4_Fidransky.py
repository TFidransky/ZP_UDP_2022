
class CharFrequencyAnalyzer:
        # Constructor that prompts user for input string.
    def __init__(self, string):
        self.string = string.upper()
        self.unwanted_chars = ".,:!?_-;%ˇ´<>'(){}[]\" "

        # Counts the frequency of each character in the input string and prints the results in descending order (from most frequent to least frequent).
            # If the character didnt appear yet, it will give that character value 1, if it did appear prior to that appearance, it will add 1 to its current value.
            # The program doesn't count special symbols like . , : and simillar. It could be modified so it would count only letters from specific alphabets and/or numbers, 
            # but it would not be as universal, because different alphabets use specific symbols, such as ř or š, that are not universally used and therefore it would be hard to implement a universal counter
        # Lastly, the function returns a list of characters sorted from the most frequent to the least frequent. This list is used in the print function.
    def char_freq(self):
        char_freq = {}

        for char in self.string:
            if char not in self.unwanted_chars:
                if char not in char_freq:
                    char_freq[char] = 1
                else:
                    char_freq[char] += 1

        self.char_freq = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

        return char_freq

        # This function simply prints the list of characters and their usage in the sentence inputted by user.
    def print_char_freq(self, char_freq):
        for char, freq in char_freq:
            print(f"{char}: {freq}")
        
        # This makes sure, that users inputs something in the terminal. If he doesn't, the program will ask again, until the user enters something.
            # If the user enters only the symbols that are in the variable "unwanted_chars", the program will again give error code and prompt user to enter something again.        
    def get_valid_input(self):
        string = input("Input the sentence of which you want to know the frequency of each character: ")
        while string.strip() == "":
            print("No input was recorded, try again.")
            string = input("Input the sentence of which you want to know the frequency of each character: ")
        for char in self.unwanted_chars:
            string = string.replace(char,'')
        if string.strip() != "":
            return string
        else:
            print("Invalid input. There were only unwanted characters in your input. Try again.")
            return self.get_valid_input()

      # Main function that calls the char_freq function if a valid input string is provided.
    def main(self):
        self.string = self.get_valid_input()
        self.char_freq()
        self.print_char_freq()

    # First the istance of CharFrequencyAnalyzer class is created with empty string as input. Then the main function of this instance gets called, 
    # which controls the input and proper calling of individual functions.
analyzer = CharFrequencyAnalyzer('')
analyzer.main()

