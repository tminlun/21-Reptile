# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/11 0011 20:50'

import requests, json, os, time, random

# 分词
import jieba


# 储存数据的文件路径
comment_file_path = os.path.join(os.getcwd(), 'jd_comment.txt')


def get_url(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
            'Referer':'https://item.jd.com/1263013576.html'
        }
        response = requests.get(url=url, headers=headers)
        text = response.content.decode("gbk")
        return text
    except:
        print("爬取失败")


def spider_commit(text):
    ''' 解析数据 '''

    # 全部数据，过滤[26:-2]
    html = json.loads(text[26:-2])
    comments = html['comments']

    datas = []

    # 解析
    for comment in comments:
        # 写入txt
        with open(comment_file_path, 'a+', encoding='utf-8') as f:
            # 以追加写入数据
            f.write(comment['content'] + '\n')


def cut_word():
    '''
    数据进行分词
    :return: 分词后的数据
    '''
    with open(comment_file_path, encoding='utf-8') as f:
        comment_text = f.read()
        wordList =jieba.cut(comment_text, cut_all=True)  # cut_all  把句子中所有的可以成词的词语都扫描出来
        wl = " ".join(wordList)
        return wl


def create_word_cloud():
    '''
    生成词云
    :return:
    '''
    import numpy as np
    from PIL import Image
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

    # 设置词云图片形状
    coloring = np.array(Image.open('wawa.jpg'))
    # 设置词云配置
    wordcloud = WordCloud(background_color="white", width=2000, mask=coloring,random_state=42,
                          height=860, margin=2,scale=4,max_font_size=50)
    # 生成词云
    wordcloud.generate(cut_word())

    # 得到词云
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()


def main():
    # 写入数据之前，清空之前的数据
    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)

    for i in range(0, 1):
        # 获取网页
        url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv6930&productId=1263013576&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1".format(i)
        text = get_url(url)

        # 爬取数据
        spider_commit(text)
        # 模拟爬虫，睡眠一段时间，防止封ip
        time.sleep(random.random() * 5)




if __name__ == '__main__':
    main()
    create_word_cloud()