#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 歌唱类，创建对象
class Song():

    # 默认初始化方法，new新对象时执行
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_the_song(self):
        for line in self.lyrics:
            print(line)

# 创建对象并传入歌词
happy_bday = Song([
    "Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"
    ])

# 同上
bulls_on_parade = Song([
    "They rally around the family",
    "With pockets full of shells"
    ])

# 执行唱歌的方法
happy_bday.sing_me_the_song()

# 同上
bulls_on_parade.sing_me_the_song()
