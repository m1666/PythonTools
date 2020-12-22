import requests


def spider(sn):
    """ 爬取淘宝网的图书数据 """
    url = 'https://s.taobao.com/api?ajax=true&m=customized&sourceId=tb.index&q={0}'.format(sn)
    rest = requests.get(url).json()
    print(rest)
    bk_list = rest['API.CustomizedApi']['itemlist']['auctions']
    print(len(bk_list))
    for bk in bk_list:
        # 标题
        title = bk['raw_title']
        # 价格
        price = bk['view_price']
        # 购买链接
        link = bk['detail_url']
        # 店铺
        store = bk['nick']
        print('{title}: {price}: {link}: {store}'.format(
            title=title,
            price=price,
            link=link,
            store=store
        ))


if __name__ == '__main__':
    sn = '9787544281096'
    spider(sn)
