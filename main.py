from stats import *
import sys

def main():
    num = num_words()
    letters = make_strings()
    print(f"============BOOKBOT============\n Analyzing book found at books/frankenstein.txt... \n ----------- Word Count -----------\n Found {num} total words \n -------- Character Count --------")
    for i in letters:
        print(f"{i}: {letters[i]}")

main()