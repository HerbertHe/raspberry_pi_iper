#!/usr/bin/env python
# -*- coding:utf-8 -*-

import python_email as email
import online_check as online
import inside_ip as in_ip


def upper():
    ip = in_ip.checker('usb0')
    email.email_function("usb0:" + ip)
    print(ip)


if __name__ == "__main__":
    while not online.isOnline():
        continue
    while not in_ip.checker('usb0'):
        continue
    upper()
    print("成功！")
