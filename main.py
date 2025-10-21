from stats import get_num_words
from stats import count_chars
from stats import sort_alpha_counts
import sys

def get_book_text(path_to_file):
    #print(path_to_file)
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path =  sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    count = count_chars(book)
    #sorted_count = sort_alpha_counts(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_alpha_counts(count)
    print("============= END ===============")

main()