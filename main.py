print("greetings boots")

from collections import Counter
from stats import get_num_words

path_to_file = 'books/frankenstein.txt'

with open(path_to_file) as f:
    file_contents = f.read()

def word_count(text):
    return len(text.split())

def char_count(text):
    return Counter(text.lower())

print(f'''
{char_count(file_contents)=}
{word_count(file_contents)=}
# {char_count(file_contents)=}
# {char_count(file_contents)=}
''')

