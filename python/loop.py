#! /usr/bin/env python3
# pass是空语句，是为了保持程序结构的完整性
# pass不做任何事情，一般用作占位语句

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1到%d之和为：%d" % (n, sum))

# infinite loop
var = 1
while var == 1:
    var = int(input("输入一个数字："))
    print("你输入的数字是%d" % var)

# for eg
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

# break in for
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据" + site)

for i in range(4, 9):
    print(i)
