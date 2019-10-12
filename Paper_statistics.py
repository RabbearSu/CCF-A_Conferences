import numpy as np
import string
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import time
import nltk
from nltk.corpus import stopwords
from collections import Counter
# nltk.download('stopwords')


# 读取txt文件
acl_2017 = "ACL\\txt\\paper_list_2017.txt"
acl_2018 = "ACL\\txt\\paper_list_2018.txt"
acl_2019 = "ACL\\txt\\paper_list_2019.txt"

icml_2017 = "ICML\\txt\\paper_list_2017.txt"
icml_2018 = "ICML\\txt\\paper_list_2018.txt"
icml_2019 = "ICML\\txt\\paper_list_2019.txt"

# Get
def getKeyCounter(txt_path):
    # 打开txt文件
    with open(txt_path, "r", encoding='UTF-8') as f:
        lines = f.read()
        title = lines.split('\n')
        f.close()

    # print(title)
    # print("The number of total accepted paper titles : ", len(title))

    # print(stopwords.words('english'))
    stopwords_deep_learning = ['learning', 'network', 'neural', 'networks', 'deep', 'via', 'using', 'convolutional',
                               'single']
    keyword_list = []

    for i in range(len(title)):
        # print(i, "th paper's title : ", title[i])
        word_list = title[i].split(" ")
        word_list = list(set(word_list))

        word_list_cleaned = []
        for word in word_list:
            word = word.lower()
            if word not in stopwords.words('english') and word not in stopwords_deep_learning:  # remove stopwords
                word_list_cleaned.append(word)

        for k in range(len(word_list_cleaned)):
            keyword_list.append(word_list_cleaned[k])

    keyword_counter = Counter(keyword_list)
    print(keyword_counter)
    print('{} different keywords before merging'.format(len(keyword_counter)))

    # Merge duplicates: CNNs and CNN
    duplicates = []
    for k in keyword_counter:
        if k + 's' in keyword_counter:
            duplicates.append(k)
    for k in duplicates:
        keyword_counter[k] += keyword_counter[k + 's']
        del keyword_counter[k + 's']
    # print('{} different keywords after merging'.format(len(keyword_counter)))
    # print(keyword_counter)
    return keyword_counter


# Show N most common keywords and their frequencies
def showPicture(keyword_counter):
    num_keyowrd = 75
    keywords_counter_vis = keyword_counter.most_common(num_keyowrd)

    plt.rcdefaults()
    fig, ax = plt.subplots(figsize=(8, 18))

    key = [k[0] for k in keywords_counter_vis]
    value = [k[1] for k in keywords_counter_vis]
    y_pos = np.arange(len(key))
    ax.barh(y_pos, value, align='center', color='green', ecolor='black', log=True)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(key, rotation=0, fontsize=10)
    ax.invert_yaxis()
    for i, v in enumerate(value):
        ax.text(v + 3, i + .25, str(v), color='black', fontsize=10)
    # ax.text(y_pos, value, str(value))
    ax.set_xlabel('Frequency')
    ax.set_title('ACL 2019 Submission Top {} Keywords'.format(num_keyowrd))
    plt.show()
    return keyword_counter


acl_2017_key_counter = getKeyCounter(acl_2017)
acl_2018_key_counter = getKeyCounter(acl_2018)
acl_2019_key_counter = getKeyCounter(acl_2019)

