import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text():
    with open(book_path, "r") as f:
        return f.read()



def num_words():
    f = get_book_text()
    return len(f.split())

def make_strings():
    letters = {}
    text = get_book_text()
    words = text.split()
    for word in words:
        for char in word:
            if char.isalpha():
                char = char.lower()
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1
    return letters