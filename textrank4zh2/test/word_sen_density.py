# !/user/bin/env python3
# _*_ encoding='utf-8' _*_

# #-------------------------------------------------------------#
# 优化1：利用关键词重要性对句子重要度重排序
# 优化2：单字词不参与句子重排过程
# 优化3：重复句子去重
# 优化4：单个词构成的句子，不能视为正常句子，需削弱
# #-------------------------------------------------------------#

import codecs
from itertools import count
import math
from utils.FastTextRank4Word2 import FastTextRank4Word
from utils.FastTextRank4Sentence2 import FastTextRank4Sentence


def summary_words(text):
    word_model = FastTextRank4Word(tol=0.0001, window=3, window_strict=1)
    w_score, words_part = word_model.summarize(text, 10)
    all_w_score = word_model.scores
    all_words = word_model.words
    words_tmp = zip(all_w_score, count())
    words_tmp = sorted(words_tmp, key=lambda d: d[0], reverse=True)
    words_st = [(all_words[i], score) for score, i in words_tmp if len(all_words[i]) > 1]  # 过滤单字

    return words_st


def summary_sens(text):
    sen_model = FastTextRank4Sentence(use_w2v=False, tol=0.0001)
    sen_score, sens_part = sen_model.summarize(text, 4)
    all_sen_score = sen_model.scores
    all_sens = sen_model.sens
    sens_tmp = zip(all_sen_score, count())
    sens_tmp = sorted(sens_tmp, key=lambda d: d[0], reverse=True)
    sens_tmp = [(all_sens[i], score) for score, i in sens_tmp]

    # 去重，去非句
    sens_st = []
    existence = []
    for sen, score in sens_tmp:
        if sen not in existence and len(sen) > 2:  # 先展示原始情况
            existence.append(sen)
            sens_st.append((sen, score))

    return sens_st


def get_summary(words_st, sens_st):
    summary_tmp = []
    for sen, sen_weight in sens_st:
        weight_tmp = 0.0
        for word, score in words_st:
            if word in sen:
                # weight_tmp += math.log2(score)*(len(word)/2)  # 词长强化
                weight_tmp += math.log2(score+0.5) * (len(word) / 2)  # 词长强化
        weight = sen_weight*(1+weight_tmp)
        summary_tmp.append((sen, weight))

    summary_tmp = sorted(summary_tmp, key=lambda d: d[1], reverse=True)
    # 去重，去非句
    summary_st = []
    existence = []
    for sen, score in summary_tmp:
        if sen not in existence and len(sen) > 3:
            existence.append(sen)
            summary_st.append((sen, score))

    return summary_st


if __name__ == "__main__":
    data_path = r'../data/'
    # file_type = 'customer_'
    file_type = 'text'

    start = 1
    end = 100
    for i in range(start, end):
        file = data_path + file_type + str(i) + '.txt'
        text = codecs.open(file, 'r', 'utf-8').read()
        file_size = len(text.split())
        if file_size < 10:
            print('size of %s is %d' % (file, file_size))
            # continue

        # 获取有序关键词和有序句子
        sens_st = summary_sens(text)
        words_st = summary_words(text)
        summary_st = get_summary(words_st, sens_st)

        # print('id2word', all_w_score)
        # print('all_words', words_st)
        print('<--------------------------------------------->')
        print('all_sens', sens_st)
        print('<=============================================>')
        print('summary_st', summary_st)

        input('Next:')

    # print('sen_part', sens_part)
