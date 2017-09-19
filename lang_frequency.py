import re
import sys
import operator


def load_data(filepath):
    with open(filepath, 'r', encoding='UTF-8') as text_string:
        return text_string.read().lower()


def get_most_frequent_words(text_string):
    frequency_dict = {}
    match_pattern = re.findall(r'(\b[a-z]+\b|\b[а-я]+\b)', text_string)
    for word in match_pattern:
        count = frequency_dict.get(word, 0)
        frequency_dict[word] = count + 1
    return frequency_dict


def sort_frequency(frequency_dict):
    frequency_list_sorted = sorted(frequency_dict.items(), key=operator.itemgetter(1), reverse=True)
    return frequency_list_sorted


def pprint_frequency(frequency_list):
    for word in frequency_list:
        print(word[0], '-', word[1])

if __name__ == '__main__':
    text = load_data(sys.argv[1])
    frequency_dict = get_most_frequent_words(text)
    frequency_list = sort_frequency(frequency_dict)
    pprint_frequency(frequency_list)
