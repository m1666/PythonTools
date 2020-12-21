import json


def python_to_json():
    """ 将python对象转换成json """
    d = {
        'name': 'python书籍',
        'price': 62.3,
        'is_valid': True
    }
    rest = json.dumps(d, indent=4)
    print(rest)


def json_to_python():
    """ 将json转换成python """
    data = '''
    {"name": 
    "Python书籍","origin_price": 66,"pub_date": "2020-11-11 18:00:00","store": ["京东", "淘宝"],"author": ["张三", "李四", "王五"],"is_valid": true,"is_sale": false,"meta": {"isbn": "abc-123","pages": 300},"desc": null}
'''

    rest = json.loads(data),
    print(rest)
    print(rest[0]['name'])


def json_to_python_from_file():
    """ 从文件读取内容，并转换成python对象 """
    file = open('./static/test.json', 'r', encoding='utf-8')

    string = file.read()
    print(string)
    rest = json.loads(string)
    print(rest)

    file.close()


if __name__ == '__main__':
    # python_to_json()
    # json_to_python()
    json_to_python_from_file()
