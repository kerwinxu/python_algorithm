# python
# -*- coding: utf-8 -*-
# @FileName : 堆栈.py
# @author : kerwin xu
# @created : 2019-10-27T19:46:21.555Z+08:00
# @last-modified : 2019-10-27T19:46:32.139Z+08:00
# @description :
# 这个实现的是简单的堆栈。
# 简单的堆栈只是包含如下的东西
# 初始化
# 判断是否为空
# 压栈
# 出栈
# 取得最后的元素。不删除。

# import .单向链表.KList as KList

import 单向链表


class KStack(单向链表.KList):
    """
    我做的一个简单的堆栈类
        :param KList: 
    """
    def __init__(self):
        """
        初始化
            :param self: 
        """
        # 只是简单的调用父类的构造方法。
        super(KStack,self).__init__()
        pass

    def is_empty(self):
        """
        判断是否为空
            :param self: 
        """
        return super(KStack,self).is_empty()

    def push(self, value):
        """
        压栈
            :param self: 
            :param value: 
        """
        self.append(value)

    def pop(self):
        """
        出栈
            :param self: 
        """
        # 首先判断是否是空栈吧
        if self.is_empty():
            return None
        else:
            _last_one = self._tail
            # 然后删除最后1位
            self.delete(self.len() - 1)
            return _last_one.value

    def top(self):
        """
        取得最后的一项。
            :param self: 
        """
        # 首先判断是否是空栈吧
        if self.is_empty():
            return None
        else:
            _last_one = self._tail
            return _last_one.value


if __name__ == "__main__":
    s = KStack()
    s.push(1)
    s.push(2)
    s.push(3)
    print("top：{0}".format(s.top()))
    print("最新的一项是：{0}".format(s.pop()))
    print("最新的一项是：{0}".format(s.pop()))
    print("最新的一项是：{0}".format(s.pop()))
    print("最新的一项是：{0}".format(s.pop()))