# 查询指数的循环例子
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "等于", x, '*', n // x)
            break
    else:
        print(n, '是质数')

for letter in 'Runoob':
    if letter == 'o':
        pass
    print('当前字母：', letter)

print("Good bye!")