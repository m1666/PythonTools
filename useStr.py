
def format_str():
    """ 格式化字符串 """
    name = "张三"
    print("欢迎您，%s" % name)

    num = 12.33
    print("输入的数字是：%.2f" % num)
    no = 33
    print("您的编号是：%04d" % no)

    t = (1, 2, 3, 4)
    print("您输入的元组是：%s" % str(t))

    print("您的姓名：%(name)s" % {'name': name})


def format_str_now():
    """ 使用format格式化字符串 """
    # 使用位置
    print('欢迎您，{0}，{1}  --{0}'.format('张三', '好久不见'))
    # 使用名称
    dic = {
        'username': '李四',
        'no': 88,
    }
    print('您好，{username}, 您的编号是{no}'.format(username='张三', no='66'))
    print('您好，{username}, 您的编号是{no}'.format(**dic))

    # 格式化元组
    point = (1, 6)
    print('坐标位置：{0[0]}:{0[1]}'.format(point))

    # 格式化类
    user = User('王五', 23)
    print(user.show())
    print(user)


class User(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def show(self):
        return '用户名：{self.username}, 年龄：{self.age}'.format(self=self)

    def __str__(self):
        return self.show()


if __name__ == '__main__':
    # format_str()
    format_str_now()
