
from collections import Counter

def count_chars_file(file, output):
    with open("text/{0}".format(file), "r") as txt:
        result = Counter()
        for line in txt:
            line = line.lower()
            a = [i for i in line if re.match("[а-я]+", i)]
            result += Counter(a)
    output.put(result)