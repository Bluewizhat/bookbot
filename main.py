from stats import words_in_text
from stats import letter_count
from stats import sort_counts
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) == 2:
        num_word = words_in_text(get_book_text(sys.argv[1]))
        letter_dic = letter_count(get_book_text(sys.argv[1]))
        sorted_dic = sort_counts(letter_dic)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_word} total words")
        print("--------- Character Count -------")
        for count in sorted_dic:
            if count["char"].isalpha():
                print(f"{count['char']}: {count['num']}")
            else:
                continue
        print("============= END ===============")
        return
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
