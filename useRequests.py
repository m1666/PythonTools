import requests

def get_book(sn):
    """ 获取书的信息 """
    url = 'http://search.dangdang.com/'
    rest = requests.get(url,params={
        'key': sn,
        'act': 'input'
    })
    print(rest.text)
    # json方式获取数据
    # rest.json()
    print(rest.status_code)
    print(rest.encoding)


if __name__ == '__main__':
    get_book('9787544281096')