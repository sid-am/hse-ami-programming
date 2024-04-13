import math


def comparing_children(index):
    left_child = segment_tree[l_child(index)]
    right_child = segment_tree[r_child(index)]
    ans = max(left_child[2], right_child[2], left_child[1] + right_child[0])
    if left_child[3]:
        left_even = left_child[0] + right_child[0]
    else:
        left_even = left_child[0]

    if right_child[3]:
        right_even = right_child[1] + left_child[1]
    else:
        right_even = right_child[1]
    flag = left_child[3] and right_child[3]
    return [left_even, right_even, ans, flag]


def parent(index):
    return (index - 1) // 2


def l_child(index):
    return 2 * index + 1


def r_child(index):
    return 2 * index + 2


def seg_row(v, vl, vr, left, right):
    if vr <= left or right <= vl:
        return [0, 0, 0, 0]
    if left <= vl and vr <= right:
        return segment_tree[v]
    median = vl + (vr - vl) // 2

    left_child = seg_row(l_child(v), vl, median, left, right)
    right_child = seg_row(r_child(v), median, vr, left, right)
    ans = max(left_child[2], right_child[2], left_child[1] + right_child[0])
    if left_child[3]:
        left_even = left_child[0] + right_child[0]
    else:
        left_even = left_child[0]

    if right_child[3]:
        right_even = right_child[1] + left_child[1]
    else:
        right_even = right_child[1]
    flag = left_child[3] and right_child[3]
    return [left_even, right_even, ans, flag]


def replace(index, value):
    if value % 2 == 0:
        segment_tree[index] = [1, 1, 1, 1]
    else:
        segment_tree[index] = [0, 0, 0, 0]
    while index != 0:
        index = parent(index)
        segment_tree[index] = comparing_children(index)


n = int(input())

segment_tree = [[0, 0, 0, 0]
                for _ in range(2 ** math.ceil(math.log2(n) + 1) - 1)]
tree_len = len(segment_tree)
start = tree_len // 2

nums = list(map(int, input().split()))
for i in range(n):
    if nums[i] % 2 == 0:
        segment_tree[i + start] = [1, 1, 1, 1]
    else:
        segment_tree[i + start] = [0, 0, 0, 0]
for i in range(start - 1, -1, -1):
    segment_tree[i] = comparing_children(i)

requests_num = int(input())
for _ in range(requests_num):
    request, L, R = map(int, input().split())
    if request == 1:
        print(seg_row(0, start, tree_len, L + start, R + start + 1)[2])
    else:
        replace(L + start, R)
