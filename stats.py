def sort_on(items):
    return items["num"]

def words_in_text(book_contents):
    word_list = book_contents.split()
    return len(word_list)

def letter_count(book_contents):
    letter_counts = {}

    word_list = book_contents.split()
    for word in word_list:
        for letter in word:
            if letter.lower() in letter_counts:
                letter_counts[letter.lower()] += 1
            else:
                letter_counts[letter.lower()] = 1
    return letter_counts

def sort_counts(letter_count_dic):
    dic_to_sort = []
    for key in letter_count_dic:
        dic_to_sort.append({"char": key, "num": letter_count_dic[key]})
    dic_to_sort.sort(reverse = True, key = sort_on)
    return dic_to_sort