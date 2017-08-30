# 股票最大化收益问题
# 转换成每日变化
# ==> A的和最大的连续非空子数组
def find_max_crossing_subarray(a, low, mid, high):
    left_sum = a[mid]
    max_left = mid
    tem_sum = 0
    for i in range(mid, low-1, -1):
        tem_sum = tem_sum + a[i]
        if tem_sum > left_sum:
            left_sum = tem_sum
            max_left = i

    right_sum = a[mid+1]
    max_right = mid + 1
    tem_sum = 0
    for i in range(mid+1, high+1):
        tem_sum = tem_sum + a[i]
        if tem_sum > right_sum:
            right_sum = tem_sum
            max_right = i

    sum_max = left_sum + right_sum
    return max_left, max_right, sum_max


def find_maximum_subarray(a, low, high):
    if low == high:
        return low, high, a[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(a, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(a, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        if right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        if cross_sum >= left_sum and cross_sum >= right_sum:
            return cross_low, cross_high, cross_sum

if __name__ == '__main__':
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    #find_maximum_subarray(a, 0, len(a))
    #print(a)
    #print(find_max_crossing_subarray(a, 0, 7, len(a)-1))
    print(find_maximum_subarray(a, 0, len(a)-1))
