if __name__ == '__main__':
    """
    多行输入格式化
    """
    a = ""
    b = input()
    while b != ":w":
        a = a + '\"' + b + '\"' + ',\n'
        b = input()
    f = open("method.txt", "w")
    f.write(a)
