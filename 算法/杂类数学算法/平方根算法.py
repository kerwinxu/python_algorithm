# python
# -*- coding: utf-8 -*-
# @FileName : 平方根算法.py
# @author : kerwin xu
# @created : 2019-11-13T23:03:37.562Z+08:00
# @last-modified : 2019-11-13T23:12:32.211Z+08:00
# @description : 这个是一个简单的求解平方根的算法。
#


def iter_improve(update, test, guess=1):
    """
    用迭代改进法求解某些值。
        :param update: 
        :param test: 
        :param guess=1: 
    """
    while not test(guess):  # 精度是否符合要求了
        guess = update(guess)  # 继续改进
    return guess


def square_root(x):
    def average(a, b):
        return (a + b) / 2

    def update(guess):
        return average(guess, x / guess)

    def approx_dq(a, b, tolerance=0.0001):
        return abs(a - b) < tolerance

    def test(guess):
        return approx_dq(guess * guess, x)

    return iter_improve(update, test, guess=x / 2)


if __name__ == '__main__':
    pass
    print(square_root(101))
