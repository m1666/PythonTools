import requests
from lxml import html


book_list = []


def get_book_list(sn, page):
    """ 爬取京东的图书数据 """
    url = 'https://search.jd.com/Search?keyword={sn}&page={page}'.format(sn=sn, page=page)
    # 获取html文档
    header = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'http://search.jd.com',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Host': 'gia.jd.com',
        'Proxy-Connection': 'keep-alive'
    }
    html_doc = requests.get(url, headers=header, verify=False).text
    # 获取xpath对象
    selector = html.fromstring(html_doc)
    # 获取图书列表集合
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(ul_list)


# def spider():


if __name__ == '__main__':
    sn = '9787544281096'
    page = 1
    get_book_list(sn, page)