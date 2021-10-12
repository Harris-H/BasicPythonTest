if __name__ == '__main__':
    a = [1, 2, 3]
    b = ['a', 'b', 'c']
    c = zip(a, b)
    print(type(c))  # <class 'zip'>
    print(c)  # 返回一个zip对象 <zip object at 0x000002757713EB00>
    print(dict(c))  # 转为dict
    # print(list(c))   此写法错误,返回空列表
    i1, i2 = zip(*zip(a, b))
    print(list(zip(*zip(a, b)))) # [(1, 2, 3), ('a', 'b', 'c')]
    print(*zip(a, b))  # (1, 'a') (2, 'b') (3, 'c')
    print(i1, i2)  # (1, 2, 3) ('a', 'b', 'c')　解压
    nums = ['flower', 'flow', 'flight']
    for i in zip(*nums):
        print(i)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(list(zip(*matrix)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)] 取列
    d = ['Herio', 'dsadsa', 'harris']
    print(list(zip(a, b, d)))  # 返回以元组为元素的列表
