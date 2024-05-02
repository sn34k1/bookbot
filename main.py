def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    print("Total Letter Counts:")
    for k, v in num_letters.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("")
    print("--- End of report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    import collections
    text_lower = text.lower()
    letter_counts = collections.Counter(text_lower)
    
    keys = list(letter_counts.keys())
    keys.sort()
    sorted_counts = {i: letter_counts[i] for i in keys}
    
    return sorted_counts
        



main()