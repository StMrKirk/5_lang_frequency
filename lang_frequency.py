import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as text_string:
        return text_string.read().lower()


def get_most_frequent_words(text_string):
    match_pattern = re.findall(r'\w+', text_string)
    return Counter(match_pattern).most_common()


def pprint_frequency(frequency_list):
    for word in frequency_list:
        print(word[0], '-', word[1])


if __name__ == '__main__':
    text = load_data(sys.argv[1])
    frequency_dict = get_most_frequent_words(text)
    pprint_frequency(frequency_dict)

