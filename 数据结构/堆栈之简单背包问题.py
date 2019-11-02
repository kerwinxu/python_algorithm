# python
# -*- coding: utf-8 -*-
# @FileName : 堆栈之简单背包问题.py
# @author : kerwin xu
# @created : 2019-10-29T21:35:07.327Z+08:00
# @last-modified : 2019-10-29T21:35:07.327Z+08:00
# @description : 问题的描述 ：一个背包中可放入重量为weight的物品，现有n件物品集合S，
# 其中物品的重量分别为 w0 , w1 , ... w_n-1 , 问题是能否从中选出若干件物品，
# 其重量之和正好等于weight , 如果存在就说明这一个背包问题有解，否则就是无解。
# 现在考虑问题的求解，
# 假设weight >= 0 , n >= 0 , 用记法 knap(weight,n)  表示n个物品相对于总重量weight的背包问题。
# 在考虑是否有解时，通过考虑一件物品的选或者不选，可以把原问题划分为两种情况
# 1. 如果不选最后一件物品（其重量为 w_{n-1} ) ,那么knap(weight,n-1)的解也就是knap(weight,n)的解，如果找到前者的解也就找到了后者的解
# 2. 如果选择最后一件物品，那么如果knap(weight-w_{n-1} , n-1) 有解，其解加上最后一项物品就是 knap(weight,n) 的解，即前者有解后者也有解。
# 在上述的两种情况下，原问题都可归结为更简单的问题，这样下去，最后可以归结为几种最简单的情况
# 1. 重量weight=0，说明找到解了
# 2. 重量weight已经小于0 ， 说明已做的安排不能得到一个解。
# 3. 重量大于0 ，但已经没有物品可用，说明依然无解。
# 这种解决方式是将负责的问题分解成简单的问题，反正对于一件物品来说，只有两种情况，一种是选择它是，而另一种是不选择。


def knap(weight, wlist, n):
    """
    docstring here
        :param weight: 背包承重
        :param wlist:  物品的重量表
        :param n: 物品数量
    """
    if weight == 0:
        # 找到解
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    # 如下是两个选择了，反正对于同一个物品，要么选择是正确的，要么不选择是正确的。
    # 但这两个选择都要试试，所以都单独用if，
    if knap(weight - wlist[n - 1], wlist, n - 1):
        # wlist的下标是从0开始的，
        print("选择第{0}个物品，重量为{1}".format(n, wlist[n - 1]))
        return True
    if knap(weight, wlist, n - 1):
        return True
    else:
        return False


if __name__ == "__main__":
    knap(18, [1, 2, 3, 4, 5, 6, 7, 8], 8)
    pass
