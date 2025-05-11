import sys

from stats import get_book_text
# Imports the function num_words from the stats.py file
from stats import num_words
# Imports the function character_count from stats.py file
from stats import character_count
from stats import char_sorting

# Gets what was input into the terminal in this case main.py and the path to the book
sys.argv
# Checks to see if both the inputs were correct and if it's long enough
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Calls functions when used
def main():
        # Prints the entirety of the file in a string to the terminal
    # print(get_book_text(filepath))
        # Prints the total number of strings found in the num_words function
    #print(f"Found {num_words(text)} total words")
        # Prints the entire non-sorted dictionary from character_count
    #print(character_count(text))
    
    # Uses the second index in the inputs (path_to_book) to determine which book to check
    path = sys.argv[1]
    # Uses file that is chosen by the path as the parameter for get_book_text
    text = get_book_text(path)
    # Uses the result of get_book_text to count the number of words
    word_count = num_words(text)
    # Uses the result of the get_book_text to make a dictionary containing all the letters in the words
    char_dict = character_count(text)
    # Uses the dictionary containing all the letters in the words an sorts them alphabetically
    sorted_chars = char_sorting(char_dict)

    def print_report(path, wordcount,sorted_chars):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")

        print("----------- Word Count -----------")
        print(f"Found {word_count} total words")

        print("--------- Character Count -------")
        for char_info in sorted_chars:
            char = char_info["char"]
            count = char_info["num"]
            if char.isalpha():
                print(f"{char}: {count}")

        print("============= END =============")
    print_report(path, word_count, sorted_chars)


main()