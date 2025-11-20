def get_num_words(book):
    return len(book.split())

def get_character_count(book):
    lower_book = book.lower()
    character_instances = {}
    for ch in lower_book:
        if ch in character_instances:
            character_instances[ch] += 1
        else:
            character_instances[ch] = 1

    return character_instances

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(characters):
    sorted_list = []
    for key in characters:
        sorted_list.append({"char": key, "num": characters[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    # print(f"Sorted List Before Sort: {sorted_list}")
    return sorted_list

def build_report(num_words, characters_list):
    report_list = [
        "============ BOOKBOT ============",
        "Analyzing book found at books/frankenstein.txt..",
        "----------- Word Count ----------",
        f"Found {num_words} total words",
    ]

    for ch in characters_list:
        if ch["char"].isalpha():
            report_list.append(f"{ch['char']}: {ch['num']}")

    report_list.append("============= END ===============")
    report = '\n'.join(report_list)
    return report
