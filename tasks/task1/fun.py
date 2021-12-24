#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fun1(num):
    def fun2():
        return num + 3
    return fun2()
