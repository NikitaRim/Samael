"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import Counter
from typing import List
import re


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding='utf-8', mode='r') as fi:
        text = fi.read().encode('utf-8').decode('unicode-escape')
        words = text.split(' ')
        finale_list = sorted(words, key=lambda x: len(set(x)), reverse=True)  #
        finale_list = finale_list[:10]  #

    return finale_list


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding='utf-8', mode='r') as file:
        counter = Counter(file.read().encode('utf-8').decode('unicode-escape'))  # Самая редкая буква учитывая регистр
    rare_letter = min(counter, key=counter.get)
    return rare_letter


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding='utf-8', mode='r') as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        string_without_letter = re.sub(r'[^!.,?:;\-\(\)\"\"]', '', text)
        quantity = len(string_without_letter)
        return quantity


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, mode='r') as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        c = 0
        for i in text:
            if i.isascii():
                c += 1
        return c


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, mode='r') as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        ascii_simbols = ''
        for i in text:
            if not i.isascii():
                ascii_simbols += i
        counter = Counter(ascii_simbols)  # Самая редкая буква учитывая регистр
        most_common_letter = max(counter, key=counter.get)
        return most_common_letter