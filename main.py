# Рефакторинг написать функции
# добавить мультипроцесиинг
# 

from corus import load_lenta
from pymystem3 import Mystem
from tqdm import tqdm
from random import choice

path = 'lenta-ru-news.csv.gz'
records = load_lenta(path)
lst = []
i = 0
for record in tqdm(records):
    lst += [r for r in record.text.split('.') if r != '']
    i += 1
    if i == 1000:
        break

stem = Mystem()
sentence = choice(lst)
sentence_analyzed = stem.analyze(sentence)
print(sentence)
print('===============================================================')
print(sentence_analyzed)

new_sentence = []
for data in sentence_analyzed:
    if 'analysis' in data:
        analysis  = data['analysis'][0]
        word_type = analysis['gr'].split(',')[0]
        if word_type in ('S', 'A', 'V'):
            new_sentence.append(analysis['lex'])
print(new_sentence)


