import requests
from lxml import html

book_list = []


def spider(ul_list, list=[]):
    for li in ul_list:
        # 标题
        title = li.xpath('a/@title')
        # print(title[0])
        # 购买链接
        link = li.xpath('a/@href')
        # print(link[0])
        # 价格
        price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        # print(price[0])
        price = '0.00' if len(price) == 0 else price[0].replace('¥', ''),
        # print(price)
        # 商家
        store = li.xpath('p[@class="search_shangjia"]/a/text()')
        store = '当当自营' if len(store) == 0 else store[0]
        list.append({
            'title': title[0],
            'price': price,
            'link': link[0],
            'store': store
        })
        # print(store)

        # print("---------------------------------")


def get_book_list(sn, page, bk_list = []):
    global book_list
    """ 爬取当当网的数据 """
    url = 'http://search.dangdang.com/?key={sn}&act=input&page_index={page}'.format(sn=sn, page=page)
    # 获取html内容
    html_doc = requests.get(url).text

    # 获取xpath对象
    selector = html.fromstring(html_doc)

    # 文本分析
    # 找到书本的列表
    ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')

    # print(len(ul_list))
    # if len(ul_list) > 0:
    #     book_list = book_list + ul_list
    #     new_page = page + 1
    #     get_book_list(sn, new_page)
    # else:
    spider(ul_list, bk_list)


if __name__ == '__main__':
    sn = '9787544281096'
    page = 1
    get_book_list(sn, page)
