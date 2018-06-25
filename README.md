# Text File Content Analyzer

**This script reads text from a file, breaks it into words and performs statistical analysis on them**

#### Features:
* Read any text file and break into words
* Count total number of words and total number of unique words
* Show most common occurring words
* Graph word occurrence frequency alphabetically
* Graph word occurrence frequency by word length
* Search/limit results with Regex
* Limit results by word length
* Include or split words with hyphens
* Include or exclude common words (i.e: a, an, at, the, etc...)

### Prerequisites:
* Python version => 3

##### List all the options:
*Execute `--help` to display options*
```./text_digest.py --help
shell#: text_digest.py [-h] [-f FILE_PATH] [-d] [-c] [-u] [-w]
                      [-o WORD_OCCURANCE_LIMIT] [-s SEARCH_FOR_WORD] [-a] [-l]
                      [-y] [-n MIN_LENGTH] [-m MAX_LENGTH] [-i] [-t]

Analyzes file text and shows stats. Allows Regex searching and
enabling/disabling attributes below. Must provide --file-path to text file.
Pass --show-all to run all stats

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PATH, --file-path FILE_PATH
                        Provide path to text file. Use -h or --help for more
                        info
  -d, --display-all, --show-all
                        Display ALL stats. Triggers if other attributes are
                        not set
  -c, --words-count     Display total number of words. Default is False
  -u, --unique-words-count
                        Display total number of UNIQUE words. Default is False
  -w, --word-occurance  Show most common words. Default is False
  -o WORD_OCCURANCE_LIMIT, --word-occurance-limit WORD_OCCURANCE_LIMIT
                        limit of top occuring words to list. Default is 10
  -s SEARCH_FOR_WORD, --search-for-word SEARCH_FOR_WORD
                        Using Regex, find specific words and number of times
                        they appear in text. (ex: --search-for-word 'whal.+')
  -a, --alphabetic-ratio
                        Print alphabetic breakdown graph. Default is False
  -l, --length-ratio    Print word length ratio graph. Default is False
  -y, --allow-hyphens   Include words with - in them (ex: chat-room). Default
                        is False
  -n MIN_LENGTH, --min-length MIN_LENGTH
                        Set minimum word length. Default is 2
  -m MAX_LENGTH, --max-length MAX_LENGTH
                        Set maximum word length
  -i, --include-common  Includes common words (ex: the,a,an,is). Default is
                        False
  -t, --file-modify-time
                        Show last time file was modified. Default is False```