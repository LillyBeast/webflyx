from stats import word_count, char_count
from sys import argv

# path_to_file = "books/frankenstein.txt"

if len(argv) < 2:
    print("Usage: python main.py <path to book>")
    exit(1)

path_to_file = argv[1]

with open(path_to_file) as f:
    file_contents = f.read()

print(
    f"""
============ BOOKBOT ============
Analyzing book found at {path_to_file}...
----------- Word Count ----------
Found {word_count(file_contents)} total words
--------- Character Count -------
{[f"{k}: {v}" for k,v in char_count(file_contents).most_common() if k.isalnum()]}
"""
)
