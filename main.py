from stats import get_num_words, char_count, sorted_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(open_to_file):
    with open(open_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    char_dict = char_count(book_text)
    #print(char_dict)
    sort_dict = sorted_dict(char_dict)
    for item in sort_dict:
        character = list(item.keys())[0]
        if character.isalpha():
            count = item[character]
            print(f"{character}: {count}")


if __name__ == "__main__":
    main()