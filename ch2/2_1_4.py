def add_binary(a, b):
    length = len(a)
    carry = 0
    for i in range(length-1, -1, -1):
        sum_bit = carry ^ a[i] ^ b[i]
        sum_dec = carry + a[i] + b[i]
        if sum_dec > 1:
            carry = 1
        else:
            carry = 0
        c.append(sum_bit)
    if carry:
        c.append(carry)
    c.reverse()

if __name__ == '__main__':
    a = [1, 0, 0, 1, 1]
    b = [1, 1, 0, 0, 1]
    c = []
    add_binary(a, b)
    print(c)
