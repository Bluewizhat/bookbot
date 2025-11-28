from stats import words_in_text
from stats import letter_count
from stats import sort_counts

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

def main():
    num_word = words_in_text(get_book_text("books/frankenstein.txt"))
    letter_dic = letter_count(get_book_text("books/frankenstein.txt"))
    sorted_dic = sort_counts(letter_dic)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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

main()
