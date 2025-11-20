def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def get_word_count(book):
    return len(book.split())

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book)
    print(f"Found {num_words} total words")

main()