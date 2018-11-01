#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
import json
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def email_function(ip):
    config_file = "config.json"
    with open(config_file) as c_file:
        info = json.load(c_file)
    from_addr = info["from_addr"]
    password = info["password"]
    to_addr = info["to_addr"]
    smtp_server = info["smtp_server"]
    msg = MIMEText(ip, 'plain', 'utf-8')
    lam_format_addr = lambda name, addr: formataddr((Header(name, 'utf-8').encode(), addr))
    msg['From'] = lam_format_addr('树莓派', from_addr)
    msg['To'] = lam_format_addr('Host', to_addr)
    msg['Subject'] = Header('IP提醒', 'utf-8').encode()
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
