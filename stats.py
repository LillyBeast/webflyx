from collections import Counter

def word_count(text):
    return len(text.split())

def char_count(text) -> Counter:
    return Counter(text.lower())