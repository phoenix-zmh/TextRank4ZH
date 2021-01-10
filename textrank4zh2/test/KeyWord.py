from utils.FastTextRank4Word2 import FastTextRank4Word
import codecs
import datetime
import types


mod = FastTextRank4Word(tol=0.0001, window=3, window_strict=1)
old_time = datetime.datetime.now()
data_path = r'../data/'
file_type = 'text'

for i in range(1, 2):
    file = data_path + file_type + str(i) + '.txt'
    text = codecs.open(file, 'r', 'utf-8').read()
    print('摘要')
    old_time = datetime.datetime.now()
    score, po = mod.summarize(text, 10)

    print('<---------------------------------------------->')
    print('score', score)
    print('get', type(po[0]), po)
    print(datetime.datetime.now() - old_time)
