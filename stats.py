def get_num_words(books):
    words = 0
    for word in books.split():
        words += 1
    return words

def char_count(book):
    book = book.lower()
    char_dict = {}
    for word in book.split():
        for letter in word:
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict

def sort_on(dict):
    return list(dict.values())[0]

def sorted_dict(dict):
    report_list = []
    for key, value in dict.items():
        list_update = {}
        list_update[key] = value
        report_list.append(list_update)
    report_list.sort(reverse=True, key=sort_on)
    return report_list