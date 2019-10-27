# python
# -*- coding: utf-8 -*-
# @FileName : 单向链表.py
# @author : kerwin xu
# @created : 2019-10-12T20:22:46.763Z+08:00
# @last-modified : 2019-10-12T20:45:09.870Z+08:00
# @description : 我这个是单向链表
# 这里需要的操作如下：
# 创建一个链表
# 判断是否为空表
# 链表的长度
# 在第一位插入元素
# 作为最后一个元素
# 在某项插入一个元素
# 删除第一个元素
# 删除最后一个元素
# 删除第几个元素
# 查找元素
# 对表中的每个元素执行操作
# 然后异常有
# 超出异常
#


class KNote():
    """
    用这个来表示保存数据的节点
    """

    def __init__(self, value, pre=None, next_=None):
        """
        构造函数，参数只需要一个值，初始化的时候，有个next表示保存下一个Knote的指针
        docstring here
            :param self: 子帧
            :param value: 这个节点的值
            :param pre : 指向上一个节点
            :param next_ : 指向下一个节点
        """
        self.value = value
        # next指向下一个数据。
        self.next = next_
        # pre 指向上一个数据
        self.pre = pre


class KList():
    def __init__(self):
        # 我这里有一个头指针、一个尾指针和一个表示数据长度的东西。
        self._head = None
        self._tail = None
        # 我这里用这个属性来记录长度，以后查找长度操作会很快。
        self._len = 0

    def is_empty(self):
        """
        判断为空
            :param self: 自身
        """
        # 我还是直接判断长度吧
        return self.len() == 0
        if self._head is None:
            return True
        return False
        pass

    def len(self):
        """
        返回长度
            :param self: 长度
        """
        return self._len
        pass

    def prepend(self, value):
        """
        在第一个位置插入
            :param self: 自身
            :param value: 值
        """
        # 这里直接调用别的函数实现
        self.insert(0, value)
        pass

    def append(self, value):
        """
        插入到最后。
            :param self: 自身
            :param value: 值
        """
        self.insert(self.len(), value)
        pass

    def insert(self, n, value):
        """
        插入操作
            :param self: 自身
            :param n: Index
            :param value: 值
        """
        # 这个首先判断是否链表为空吧
        # 如果为空，则首尾指针都要赋值
        # 首先判断是否为头部吧，头部需要复制头部指针。
        # 然后判断是否是尾部，如果是尾部，尾部指针也要重新赋值了。
        # 这里先判断一下n的有效性吧
        if n < 0:
            # 肯定无意义啦
            raise IndexError()
            pass
        if n > self.len():
            # 比长度还长，我这里下标从0开始，len-1就是最大序号了，len是可以在尾部添加的，不能再大了。
            raise IndexError()
            pass
        # 这里判断是否是第一项
        if n == 0:
            # 因为是第一项，这里要判断链表是否为空，因为不空的链表，就要操作原先第一位的指针了
            if self.is_empty():
                _new_note = KNote(value)
                self._head = _new_note
                self._tail = _new_note
            else:
                self._head = KNote(value, pre=None, next_=self._head)
                self._head.next.pre = self._head.next

        elif n == self.len():
            # 这里就表示是赋值到结尾啦
            # 赋值到结尾那很简单，只要将原先结尾的尾指针赋值到现在结尾的就可以啦。
            self._tail.next = KNote(value, self._tail)
            self._tail = self._tail.next
        else:
            # 这里就表示到中间啦。这这里的插入是插入到某一项之前。
            # 相关的数据相关是，这一项，这一项的前一项，这一项的后一项。
            _new_note = KNote(value)
            # 然后取得这一项啦。
            _old_note = self.__get_node(n)
            # 这一项的前一项
            _old_note_pre = _old_note.pre
            # 设置前一项的下一项是新的节点
            _old_note_pre.next = _new_note
            _new_note.pre = _old_note_pre
            _old_note.pre = _new_note
            _new_note.next = _old_note

            pass
        # 长度加1
        self._len = self._len + 1

        pass

    def __get_node(self, n) -> KNote:
        """取得某项
            :param self: 自身
            :param n: Index
        """
        # 这里还是要判断有效性
        if n < 0:
            raise IndexError()
            return
        elif n > self.len():
            raise IndexError()
            return
        elif n == 0:
            # 如果就是第一项呢，就直接返回啦
            return self._head
        elif n == self.len() - 1:
            # 同样，如果就是最后一项呢，就直接返回吧。
            return self._tail
        _node = self._head
        # 然后用一个循环，循环指定次数就到达指定的项啦。
        for i in range(n):
            _node = _node.next
        return _node

    def delete(self, n):
        """
        删除第几项,
            :param self: 自身
            :param n: Index
        注：我这样的删除操作有个重要问题，就是被删除的数据上的指针，我是没有更改的，
        """
        # 先判断范围
        if n < 0:
            raise IndexError()
        elif n >= self.len():
            raise IndexError()
        # 首先判断是否是首尾了。首尾的话是要设置首尾指针的
        if n == 0:
            # 要判断下一项要有啊。
            if self._head.next is not None:
                self._head = self._head.next
            else:
                # 这里就表示没有下一项啦
                self._head = self._tail = None
        elif n == self.len()-1:
            # 这里就表示n至少是1啦，至少2项。所以不用像n=0时判断啦。
            self._tail = self._tail.pre
        else:
            # 这里表示中间啦。
            # 先取得这一项
            _note = self.__get_node(n)
            # 然后取得这一项的上下指针
            _pre_note = _note.pre
            _next_note = _note.next
            # 将这个上下指针链接起来，绕过这一项，就是删除啦，
            # 至于对象的析构，由python或者手动删除
            _pre_note.next = _next_note
            _next_note.pre = _pre_note
        self._len = self._len-1
        # 这里判断是否已经为空了
        if self.len() == 0 :
            self._head = self._tail = None

    def search(self, value):
        """
        查找。
            :param self: 自身
            :param value: 值
        """
        # 我这里做省事，直接调用函数来取得每个节点
        for i in range(self.len()):
            if self.__get_node(i).value == value:
                return i
        # 如果找不到，就返回-1
        return -1

    def __str__(self):
        """
        友好的输出表示
            :param self: 自身
        """
        _str_return = []
        for i in range(self.len()):
            _str_return.append(str(self.__get_node(i).value))
        return "\n".join(_str_return)


if __name__ == "__main__":
    lst = KList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.prepend(4)
    lst.insert(2, 5)
    lst.delete(3)
    print(lst)
    pass
