import sys
from stats import count_words
from stats import count_characters
from stats import sort_character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(filepath, word_count, ordered_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in ordered_list:
        if not entry["char"].isalpha():
            continue
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
    pass

def process_args(args):
    if len(args) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return args[1]
    
def main():
    filepath = process_args(sys.argv)
    book_string = get_book_text(filepath)
    word_count = count_words(book_string)
    characters = count_characters(book_string)
    ordered_list = sort_character_counts(characters)
    print_report(filepath, word_count, ordered_list)
    
main()