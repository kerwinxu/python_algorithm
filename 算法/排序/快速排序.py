# python
# -*- coding: utf-8 -*-
# @FileName : 快速排序.py
# @author : kerwin xu
# @created : 2019-10-10T21:42:22.013Z+08:00
# @last-modified : 2019-10-10T21:53:50.155Z+08:00
# @description : 快速排序方法，基本思想是：
# 通过一趟排序将要排序的数据分割成独立的两部分，
# 其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，
# 整个排序过程可以递归进行，以此达到整个数据变成有序序列


def quicksort(lst: list):
    # 判断这个长度啦，
    if len(lst) >= 2:
        # 中间位置的数，不一定是大小中间的数
        mid = lst[len(lst) // 2]
        # 左右两边
        right = []
        left = []
        # 首先排除这个数啦
        lst.remove(mid)
        # 遍历这个列表
        for _i in lst:
            # 如果小于，就放在左边，这里假设左边的小。
            if _i < mid:
                left.append(_i)
            else:
                right.append(_i)
        # 返回值是
        return quicksort(left) + [mid] + quicksort(right)
    elif len(lst) == 2:
        # 如果有2个数，就判断是否需要交换位置。
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        pass
    else:
        return lst


if __name__ == "__main__":
    a = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    print(quicksort(a))
