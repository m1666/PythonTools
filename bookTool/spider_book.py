from spider_dangdang import get_book_list as dangdang
from spider_jd import get_book_list as jd
from spider_taobao import spider as taobao
import json


def main(sn):
    """ 图书比价工具 """
    book_list = []
    # 当当网图书
    print('当当网数据爬取完成')
    dangdang(sn, 1, book_list)

    # 京东网图书
    print('京东网数据爬取完成')
    # 淘宝网图书
    print('淘宝网数据爬取完成')
    # 排序书籍列表，价格排序格式是浮点
    book_list = sorted(book_list, key=lambda item: float(item['price']), reverse=False)
    for book in book_list:
        print(book)


if __name__ == '__main__':
    sn = input('请输入ISBN：')
    main(sn)