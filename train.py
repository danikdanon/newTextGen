import re
import json
import argparse
import os

parser = argparse.ArgumentParser(description='train')

parser.add_argument(
    '--input-dir',
    default='*',
    help='input directory'
)
parser.add_argument(
    '--model',
    default='/Users/Daniil/PycharmProjects/ГенераторТекста/dictionary',
    help='output directory'
)

namespace = parser.parse_args()

d = {}

def push(word1, word2):
    if word1 in d:
        if word2 in d[word1]:
            d[word1][word2] += 1
        else:
            d[word1][word2] = 1
    else:
        d[word1] = {}
        d[word1][word2] = 1

def StrBreak(s):   # разбивка строки, кидаю посл слово с перд строки
    s = s.lower()
    s = re.sub('ё', 'е', s)
    s = re.sub('[^а-яА-Я ]', '', s)

    words = s.split(' ')

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        if word1 != '' and word2 != '':  # сплит пробелы превращаяет в ''
            push(word1, word2) # добавляю word2 в d[word1]



def MakeDict():
    f = open(namespace.input_dir, 'r')
    LastWord = ''
    for line in f:
        LastWord = StrBreak(line)
    f.close()

if namespace.input_dir == '*':
    print('finish your text with *** symbol at new line')
    line = input()
    while line != '***':
        StrBreak(line)
        line = input()
else:
    MakeDict()

with open(args.model, 'w') as file:
    json.dump(d, file)


if __name__ == "__main__":
    main()