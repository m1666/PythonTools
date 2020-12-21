from lxml import html


def parse():
    """ 将html文件中的内容，使用xpath进行提取 """
    # 1、读取文件中的内容
    file = open('./static/index.html', 'r', encoding='utf-8')
    htmlStr = file.read()

    selector = html.fromstring(htmlStr)
    # 2、解析h3标题
    h3 = selector.xpath('/html/body/h3/text()')
    print(h3[0])
    # 3、解析ul下面的内容
    ul = selector.xpath('/html/body/ul/li')
    # ul = selector.xpath('//ul/li')
    print(len(ul))
    for li in ul:
        print(li.xpath('text()')[0])

    # 4、解析ul指定的元素值
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(ul2[0])

    # 5、解析a标签的内容
    a = selector.xpath('//div[@id="container"]/a')
    # a标签内容
    print(a[0].xpath('text()')[0])
    # href属性
    print(a[0].xpath('@href')[0])
    # title属性
    print(a[0].xpath('@title')[0])

    # 6、解析最后一个p标签
    p = selector.xpath('/html/body/p[last()]/text()')
    print(p[0])

    file.close()


if __name__ == '__main__':
    parse()