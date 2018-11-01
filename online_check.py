#!/usr/bin/env python
# -*- coding:utf-8 -*-

import platform
import subprocess


def getOpeningSystem():
    return platform.system()


def isOnline():
    userOs = Utils.getOpeningSystem()
    try:
        if userOs == "Windows":
            subprocess.check_call(["ping", "-n", "2", "www.baidu.com"], stdout=subprocess.PIPE)
        else:
            subprocess.check_call(["ping", "-c", "2", "www.baidu.com"], stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        print("网络未连通！请检查网络")
        return False


