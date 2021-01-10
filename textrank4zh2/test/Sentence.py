from utils.FastTextRank4Sentence2 import FastTextRank4Sentence
import codecs
import datetime


mod = FastTextRank4Sentence(use_w2v=False, tol=0.0001)
old_time = datetime.datetime.now()
data_path = r'../data/'
file_type = 'text'

for i in range(1, 2):
    file = data_path + file_type + str(i) + '.txt'
    text = codecs.open(file, 'r', 'utf-8').read()
    print('摘要'+str(i+1)+':')
    old_time = datetime.datetime.now()
    score, po = mod.summarize(text, 4)

    print('<---------------------------------------------->')
    print('score', score)
    print('get', type(po[0]), po)
    print(datetime.datetime.now() - old_time)
