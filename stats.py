
# Defines the get_book_text function so it can be called by main
# Function reads the file
def get_book_text(path):
    # Opens the file at filepath
    with open(path) as f:
        # Reads the file that is defined by the filepath and turns it into a string
        file_contents = f.read()
    # Returns the result of the string, so it can be used by the function when called
    return file_contents


# Function counts the number of words in the file and prints as number
def num_words(text):
    # Splits the text variable that was input into the function into individual strings
    words = text.split()
    # Returns the number of individual strings in the words variable
    return len(words)

# Function that counts every character in the text and then saves them in a dictionary with how many times they show up
def character_count(text):
    # Create empty dictionary
    letters = {}
    # Set all letters from the strings of the converted text from get_book_text to lower case
    lower_case = text.lower()
    # For every character in the lower_case strings, check to see if it is already in the letters dictionary
    for char in lower_case:
        # If the character's in the letters dictionary, increase its count by 1
        if char in letters:
            letters[char] += 1
        # If the character isn't in the letters dictionary, add it to the dictionary and set its count to 1
        else:
            letters[char] = 1
    # Returns the letters dictionary filled with how many there are of each letter
    # Key = letter, value = amount
    return letters


# Function that sorts the characters from the character_count function
def char_sorting(char_dict):
    # Creates an empty list
    char_list = []
    # For each character and its count in the dictionary do this
    # Char is assigned to the current key
    # Count is assigned to the current value
    for char, count in char_dict.items():
        # Create an individual dictionary for this character
        # Would end up looking something like {"char": "a", "num": 25894}
        char_info = {"char": char, "num": count}
        # Add it to the char_list
        char_list.append(char_info)
    # How it sorts the list
    # Reverse = True, means to sort the list in descending order
    # key = lambda x, serves as the key's parameter which tells Python how to determine the value to sort by
    # x["num"], is telling the function what key it should be sorting by
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list

