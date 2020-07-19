from collections import defaultdict
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def save_word_dict(vocab, save_path):
    with open(save_path, 'w', encoding='utf-8') as f:
        for line in vocab:
            w, i = line
            print(w, i)
            f.write("%s\t%d\n" % (w, i))

# 打开清洗后的数据内容，传到words空列表
def read_data(path_1, path_2, path_3):
    with open(path_1, 'r', encoding='utf-8') as f1, \
            open(path_2, 'r', encoding='utf-8') as f2, \
            open(path_3, 'r', encoding='utf-8') as f3:
        words = []
        # print(f1)
        for line in f1:
            words = line.split()

        for line in f2:
            words += line.split(' ')

        for line in f3:
            words += line.split(' ')

    return words


def build_vocab(items, sort=True, min_count=0, lower=False):
    """
    构建词典列表
    :param items: list  [item1, item2, ... ]
    :param sort: 是否按频率排序，否则按items排序
    :param min_count: 词典最小频次
    :param lower: 是否小写
    :return: list: word set
    """
    result = []
    if sort:
        # sort by count
        dic = defaultdict(int)  # 使用collections的defaultdict类
        for item in items:
            for i in item.split(" "):
                i = i.strip()
                if not i: continue
                i = i if not lower else item.lower()
                dic[i] += 1
        # sort
        """
        按照字典里的词频进行排序，出现次数多的排在前面
        your code(one line)
        """
        dic_sorted = sorted(dic.items(), key=lambda x: x[-1], reverse=True)
        print("我输出的是字典里词频排序：", dic_sorted)

        # 根据提供的min_count对最小频次筛选，小于以及等于最小频次的予以清除，将清除后的内容存在result里
        for i, item in enumerate(dic):
            key = item[0]
            if min_count and min_count > item[1]:
                continue
            result.append(key)
    else:
        # sort by items
        for i, item in enumerate(items):
            item = item if not lower else item.lower()
            result.append(item)
    """
    建立项目的vocab和reverse_vocab，vocab的结构是（词，index）
    your code
    vocab = (one line)
    reverse_vocab = (one line)
    """
    # print(result)
    # vocab = {v: i for i, v in enumerate(result)}

    # 通过字典进行键值对互换后，将字典内的键值对输出成list形式
    vocab = list(({v: i for i, v in enumerate(result)}).items())
    # vocab = list((enumerate(result)))
    # reverse_vocab = sorted(vocab.items(), key=lambda x: x[-1], reverse=True)

    reverse_vocab = sorted(vocab, reverse=True)
    # print("我输出的是vocab:", vocab)
    # print("我输出的是reverse_vocab:", reverse_vocab)

    return vocab, reverse_vocab


if __name__ == '__main__':
    lines = read_data('{}/datasets/train_set.seg_x.txt'.format(BASE_DIR),
                      '{}/datasets/train_set.seg_y.txt'.format(BASE_DIR),
                      '{}/datasets/test_set.seg_x.txt'.format(BASE_DIR))
    vocab, reverse_vocab = build_vocab(lines)
    save_word_dict(vocab, '{}/datasets/vocab.txt'.format(BASE_DIR))