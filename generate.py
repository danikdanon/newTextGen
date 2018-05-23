import json
import random
import  argparse

d = json.load(open('dictionary',  'r'))  # загрузил созданнный словарик


parser = argparse.ArgumentParser(description='generate')

parser.add_argument(
    '--model',
    default='/Users/Daniil/PycharmProjects/ГенераторТекста/dictionary',
    help = 'file with dictionary'
)

parser.add_argument(
    '--seed',
    default='#',
    help='first word of the text'
)
parser.add_argument(
    '--length',
    default=1000,
    help='length of the text'
)
parser.add_argument(
    '--output',
    default= '/Users/Daniil/PycharmProjects/ГенераторТекста/result',
    help='output file'
)

args = parser.parse_args()


def NextWord(curr):
    if curr not in d:
        return random.choice(list(d))

    l = []   # я создаю список с дубликатами из всех слов
    for word in d[curr]:
        cnt = d[curr][word]
        l.extend([word]*cnt)

    if (len(l) == 0):
        return random.choice(list(d))
    else:
        return random.choice(l)


textlen = args.length
if args.seed == '#':
    curr = random.choice(list(d))
else:
    curr = args.seed
ans = ''
str_cnt = 0
str_len = 75
while (len(ans) < textlen):
    ans += curr + ' '
    curr = NextWord(curr)
    if (len(ans) - str_cnt*str_len > str_len):  # если строка слишком длинная
        ans += '\n'
        str_cnt += 1

with open(args.output, 'w') as file:
    file.write(ans)

