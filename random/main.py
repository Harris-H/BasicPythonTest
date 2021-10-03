import random as rd
import string

if __name__ == '__main__':
    print(rd.random())  # [0,1) 浮点数
    print(rd.randint(1, 10))  # [1,10] 整数
    print(rd.uniform(1, 5))  # [1,5] 浮点数
    l = ['小明', '小红', '小何', '小张']
    print(rd.choice(l))  # 随机从序列中选取一个
    print(rd.randrange(1, 10, 2))  # (start,end,step)  [1,10) 选奇数
    print(rd.sample('abcdefg', 3))  # 从序列中选取3个不同的 返回列表
    a = [1, 2, 3, 4, 5]  # 随机打乱
    rd.shuffle(a)
    print(a)
    # 从a-zA-Z0-9生成指定数量的随机字符：
    ran_str = ''.join(rd.sample(string.ascii_letters + string.digits, 8))
    print(ran_str)
    # 参考 https://www.runoob.com/python/func-number-random.html
