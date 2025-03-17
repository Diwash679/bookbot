def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def num_words():
    f = get_book_text()
    return len(f.split())

def main():
    text = get_book_text()
    num = num_words()
    print(text)
    print(f"{num} words found in the document")

main()