#!/usr/bin/python3
# 迭代器是一个可以记住遍历的位置的对象
# 从集合的第一个元素开始访问，知道所有的元素被访问结束
# 两个基本方法：iter()和next()
import sys
list = [1, 2, 3, 4]
it = iter(list)
it_0 = iter(list)

for x in it_0:
    print(x, end=" ")

while True:
    try:
        print(next(it))
    except:
        break
        #sys.exit()

# 使用生成器
# 生成器是一个返回迭代器的函数，只能用于迭代操作
# 简单理解就是一个迭代器
# 每次遇到yield的时候会暂停并保存所有的运行信息
# 返回yield，并在下一次执行next()方法时从当前位置继续运行
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
