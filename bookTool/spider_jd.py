import requests
from lxml import html

book_list = []


def get_book_list(sn, page):
    global book_list
    """ 爬取京东的图书数据 """
    url = 'https://search.jd.com/Search?keyword={sn}&page={page}'.format(sn=sn, page=page)
    # 获取html文档
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    html_doc = resp.text
    # 获取xpath对象
    selector = html.fromstring(html_doc)
    # 获取图书列表集合
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(len(ul_list))
    if len(ul_list) > 0:
        book_list = book_list + ul_list
        new_page = page + 1
        get_book_list(sn, new_page)
    else:
        spider(book_list)


def spider(ul_list):
    for li in ul_list:
        # 标题
        title = li.xpath('div/div[@class="p-name"]/a/@title')
        print(title[0])
        # 购买链接
        link = li.xpath('div/div[@class="p-name"]/a/@title')
        print(link[0])
        # 价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        print(price[0])
        # 店铺
        store = li.xpath('div//a[@class="curr-shop"/@title]')
        print(store[0])


if __name__ == '__main__':
    sn = '9787544281096'
    page = 1
    get_book_list(sn, page)