# python
# -*- coding: utf-8 -*-
# @FileName : 字符串查找.py
# @author : kerwin xu
# @created : 2019-10-13T20:28:00.425Z+08:00
# @last-modified : 2019-10-14T20:01:39.396Z+08:00
# @description : 这个文件是记录字符串查找方法的
#
# 如下是串比较算法

# 这个是最简单的朴素串比较算法


def native_matching(t: str, p: str):
    """
    这个是最间的的朴素穿比较算法
    docstring here
        :param t:str: 目标串
        :param p:str: 模式串
    比如：
        目标串： fjoeapfaepgjrenfpwia
        模式串： faep
    步骤：
        先将目标串和模式串对齐，顺序比较，
        发现第一个字符不相同，就将模式串右移
    """
    # 目标串和模式串的长度。
    m, n = len(p), len(t)
    i, j = 0, 0
    # 循环条件是
    # 这个i是模式串的下标，退出循环的条件有2个，
    # 一个是模式串的匹配超出了范围（都匹配成功了），而另一个就是目标串超出了范围
    while i < m and j < n:
        if p[i] == t[j]:
            # 如果字符相同，就考虑下一个字符，i和j都加1
            i, j = i + 1, j + 1
        else:
            # 这里表示不相同，就重新开始比较啦，
            # i重新设置为0，毕竟重新开始比较
            # 而j，是再返回到原先匹配的位置重新比较，这里要+1。
            i, j = 0, j - i + 1
    # 如果模式串的匹配等于长度，就表示找到这个字符串啦
    if i == m:
        # 返回原先的匹配到的位置。
        return j - i
    # 这里表示没有匹配到，
    return -1


def KMP_matching(t: str, p: str):
    """
    KMP算法实现的字符串搜索。
        Description :
        Arg :
        Returns :
        Raises	 :
    """
    pass


if __name__ == "__main__":
    t = "fjoeapfaepgjrenfpwia"
    p = "faep"
    print("找到匹配{0}".format(native_matching(t, p)))
    pass
