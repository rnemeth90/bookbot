from stats import *
import sys

def get_book_text(file_path) -> str:
    contents = ""
    with open(file_path, 'r') as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    book_text = get_book_text(book)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    sorted = sort_dict_by_value(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
        continue

if __name__ == "__main__":
    main()
    

