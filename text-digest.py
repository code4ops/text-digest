#!/usr/bin/env python3

import time, datetime
import math
import re, string
import sys, os
import argparse
from collections import Counter


def get_words(file,unique=False,sort=True,min_length=1,max_length=100,allow_hyphens=True,include_common_words=False):
    if min_length > max_length:
        raise ValueError('min_length cant be higher than max_length')

    common_words = ['the','of','a','to','an','on','at','is','are','as','have','had','from','so','be','when','there'
                    'in','and','that','this','it','but','with','was','were','for','by','or','their','in','which']
    words = []

    with open(file) as fr:
        text = fr.readlines()

    for line in text:
        if allow_hyphens:
            line = re.findall(r"\b[a-zA-Z\'-]+\b", line)
        else:
            line = re.findall(r"\b[a-zA-Z\']+\b", line)
        for word in line:
            word = word.strip("-").lower()
            if re.match("('s|[a-zA-Z\'-]+'s$)", word):
                word = word.replace("'s", '')
            if len(word) >= min_length and len(word) <= max_length:
                if not include_common_words:
                    if word not in common_words:
                        words.append(word)
                else:
                    words.append(word)

    if unique:
        if sort:
            words = sorted(list(set(words)))
        else:
            words = list(set(words))
    else:
        if sort:
            words = sorted(words)

    return words


def get_word_frequency(words,num=10,min_length=0,max_length=100,s_word=None):
    if min_length > max_length:
        raise ValueError('min_length cant be higher than max_length')

    if min_length != 0 or max_length != 100:
        filt_words = []

        for word in words:
            if len(word) >= min_length and len(word) <= max_length:
                filt_words.append(word)
        filt_counter = Counter(filt_words)
        return filt_counter.most_common(num)
    else:
        counter = Counter(words)

        if s_word:
            match_words = {}
            for word, count in counter.most_common():
                if re.match(s_word,word):
                    match_words[word] = count
            return (match_words)
        else:
            return counter.most_common(num)


def alphabetic_ratio(words):
    chars_count = {}
    chars_ratio = {}

    spaces = int(len(str(len(words)))) + 2

    for char in list(string.ascii_lowercase):
        chars_count[char] = 0
        for word in words:
            if word[0] == char:
                chars_count[char] += 1

    total_words = sum(chars_count.values())

    for char,count in chars_count.items():
        if count != 0:
            percent = float((count / total_words) * 100)
            chars_ratio[char] = float(percent)
        else:
            chars_ratio[char] = 0

    print('\nWords starting with:')
    print('-' * 150)
    for char,ratio,count in zip(chars_ratio.keys(),chars_ratio.values(),chars_count.values()):
        if ratio < 1 and ratio > 0:
            print('{0} {1:{tab}}{2} {3}'.format(char,'(' + str(count) + ')',':','|=|',tab=spaces))
        elif ratio == 0:
            print('{0} {1:{tab}}{2} {3}'.format(char,'(' + str(count) + ')',':','X',tab=spaces))
        else:
            ratio = int(ratio)
            print('{0} {1:{tab}}{2} {3}'.format(char,'(' + str(count) + ')',':',(ratio) * '|=|',tab=spaces))
    print('-' * 150)

    return chars_count


def length_ratio(words):
    min_word_len = len(min(words, key=len))
    max_word_len = len(max(words, key=len))

    words_len = {}
    length_ratio = {}

    spaces = int(len(str(len(words)))) + 2

    for length in range(min_word_len,max_word_len + 1):
        if length not in words_len:
            words_len[length] = 0
        for word in words:
            if len(word) == length:
                words_len[length] += 1

    total_words = sum(words_len.values())

    for length,count in words_len.items():
        if count != 0:
            percent = float((count / total_words) * 100)
            length_ratio[length] = float(percent)
        else:
            length_ratio[length] = 0

    print('\nLength (#Words)')
    print('-' * 150)
    for length,ratio,count in zip(length_ratio.keys(),length_ratio.values(),words_len.values()):
        if ratio < 1 and ratio > 0:
            print('{0:<4} {1:{tab}}{2} {3}'.format(length,'(' + str(count) + ')',':','|=|',tab=spaces))
        elif ratio == 0:
            print('{0:<4} {1:{tab}}{2} {3}'.format(length,'(' + str(count) + ')',':','X',tab=spaces))
        else:
            ratio = int(ratio)
            print('{0:<4} {1:{tab}}{2} {3}'.format(length,'(' + str(count) + ')',':',(ratio) * '|=|',tab=spaces))
    print('-' * 150)

    return words_len


def getmodtime(file):
    stat = os.stat(file)

    epoch_now = time.mktime(time.localtime())
    delta = (epoch_now - stat.st_mtime)
    time_elapsed = str(datetime.timedelta(seconds=math.ceil(delta))).split(":")

    print('\n{3} was last modified: {0} hours {1} minutes {2} seconds ago\n'.format(time_elapsed[0],time_elapsed[1],time_elapsed[2],file))

    return delta


if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print('This script requires Python version 3')
        print('You are using {0}.{1}.{2} {3}'.format(sys.version_info[0],sys.version_info[1],sys.version_info[2],sys.version_info[3]))
        sys.exit(-1)

    parser = argparse.ArgumentParser(description="Analyzes file text and shows stats. Allows Regex searching and enabling/disabling attributes below. Must provide --file-path to text file. Pass --show-all to run all stats")
    parser.add_argument('-f', '--file-path', help='Provide path to text file. Use -h or --help for more info', required=False)
    parser.add_argument('-d', '--display-all', '--show-all', action='store_true',help='Display ALL stats. Triggers if other attributes are not set', default=False)
    parser.add_argument('-c', '--words-count', action='store_true',help='Display total number of words. Default is False', default=False)
    parser.add_argument('-u', '--unique-words-count', action='store_true',help='Display total number of UNIQUE words. Default is False', default=False)
    parser.add_argument('-w', '--word-occurance', action='store_true',help='Show most common words. Default is False', default=False)
    parser.add_argument('-o', '--word-occurance-limit', help='limit of top occuring words to list. Default is 10', default=10)
    parser.add_argument('-s', '--search-for-word', help='Using Regex, find specific words and number of times they appear in text. (ex: --search-for-word \'whal.+\')')
    parser.add_argument('-a', '--alphabetic-ratio',action='store_true',help='Print alphabetic breakdown graph. Default is False', default=False)
    parser.add_argument('-l', '--length-ratio', action='store_true',help='Print word length ratio graph. Default is False', default=False)
    parser.add_argument('-y', '--allow-hyphens', action='store_true',help='Include words with - in them (ex: chat-room). Default is False', default=False)
    parser.add_argument('-n', '--min-length', help='Set minimum word length. Default is 2', default=2)
    parser.add_argument('-m', '--max-length', help='Set maximum word length', default=100)
    parser.add_argument('-i', '--include-common',action='store_true',help='Includes common words (ex: the,a,an,is). Default is False', default=False)
    parser.add_argument('-t', '--file-modify-time', action='store_true',help='Show last time file was modified. Default is False', default=False)
    args = parser.parse_args()

    try:
        file_name = args.file_path
    except:
        parser.print_help()
        sys.exit(0)

    if not args.file_path:
        print("Error: Path to file is required for text analysis '-f or --file-path filename'\n")
        parser.print_help()
        sys.exit(1)

    if args.display_all or (str(args).count('False') == 9 and not args.search_for_word):
        print('\nRunning all stats (-d or --show-all)\nPass -h or --help for more options\n')
        args.word_occurance = True
        args.alphabetic_ratio = True
        args.length_ratio = True
        args.words_count = True
        args.unique_words_count = True
        args.file_modify_time = True

    words = get_words(file_name,
                      unique=False,
                      sort=True,
                      allow_hyphens=args.allow_hyphens,
                      min_length=int(args.min_length),
                      max_length=int(args.max_length),
                      include_common_words=args.include_common)

    if args.word_occurance:
        freq_words = []

        for word, count in get_word_frequency(words,int(args.word_occurance_limit)):
            freq_words.append(word)

        max_len = len(max(freq_words, key=len))
        w_count = 0

        print('\nShowing Top',args.word_occurance_limit,'Words\n')
        print('{0:<3} {1:^{padding}} {2}'.format('#', 'Word', 'Count', padding=max_len + 2))
        print('{0} {1:{padding}} {2}'.format('---', max_len * '-', '-----', padding=max_len + 2))
        for word, count in get_word_frequency(words,int(args.word_occurance_limit)):
            w_count += 1
            print('{0:<3} {1:<{padding}}  {2}'.format(w_count, word, count, padding=max_len + 2))
    if args.alphabetic_ratio:
        alphabetic_ratio(words)
    if args.length_ratio:
        length_ratio(words)
    if args.words_count:
        print('\nTotal # of words:',len(words))
    if args.unique_words_count:
        print('\nTotal # of unique words: ' + str(len(set(words))) + '\n')
    if args.file_modify_time:
        getmodtime(file_name)
    if args.search_for_word:
        results = get_word_frequency(words, s_word=args.search_for_word)
        max_len = len(max(results, key=len))
        if results:
            print('\nFound match:')
            for word,count in results.items():
                print('{0:{padding}}:  {1}'.format(word, count, padding=max_len + 2))
        else:
            print('\nNo match')
