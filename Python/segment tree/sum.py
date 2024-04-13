import math


def parent(index):
    return (index - 1) // 2


def l_child(index):
    return 2 * index + 1


def r_child(index):
    return 2 * index + 2


def seg_sum(v, vl, vr, left, right):
    if vr <= left or right <= vl:
        return 0
    if left <= vl and vr <= right:
        return segment_tree[v]
    median = vl + (vr - vl) // 2
    return (seg_sum(l_child(v), vl, median, left, right) +
            seg_sum(r_child(v), median, vr, left, right))


def replace(index, value):
    segment_tree[index] = value
    while index != 0:
        index = parent(index)
        segment_tree[index] = (segment_tree[l_child(index)] +
                               segment_tree[r_child(index)])


n = int(input())

segment_tree = [0 for _ in range(2 ** math.ceil(math.log2(n) + 1) - 1)]
tree_len = len(segment_tree)
start = tree_len // 2

nums = list(map(int, input().split()))
for i in range(n):
    segment_tree[i + start] = nums[i]
for i in range(start - 1, -1, -1):
    segment_tree[i] = segment_tree[l_child(i)] + segment_tree[r_child(i)]

requests_num = int(input())
for _ in range(requests_num):
    request, L, R = map(int, input().split())
    if request == 1:
        print(seg_sum(0, start, tree_len, L + start, R + start + 1))
    else:
        replace(L + start, R)
