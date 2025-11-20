import sys
from stats import get_num_words, get_character_count, chars_dict_to_sorted_list, build_report

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    character_instances = get_character_count(book)
    sorted_list = chars_dict_to_sorted_list(character_instances)
    report = build_report(num_words, sorted_list)

    print(report)

main()