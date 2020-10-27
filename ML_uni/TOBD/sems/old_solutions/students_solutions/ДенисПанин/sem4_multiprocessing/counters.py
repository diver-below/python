
from collections import Counter

def count_chars_in_book(filename):
    chars = Counter()
    alphabet = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    path = "text/" + filename
    with open(path, "r") as txt:
        for line in txt:
            for char in line.lower():
                if char in alphabet: 
                        chars[char] += 1 
    return chars

def count_in_dir(dir_name):
    total = Counter()
    files = os.listdir(dir_name)
    for file in files:
        path = dir_name + "/" + file
        chars_in_file = Counter(count_chars_in_book(path))
        total = total+chars_in_file
    return dict(total)