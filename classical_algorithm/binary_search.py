#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : binary_search.py
# @Date    : 2022-02-18 09:29:25
# @Author  : seryte
# @Project : Algorithm-learning


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    my_list = [0, 1, 3, 5, 7, 9]
    print('result: ', binary_search(my_list, 7))
