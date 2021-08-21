#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 10:30
# @Author  : cendeavor
# @File    : net.py
# @Software: PyCharm

from urllib.parse import urlparse
import requests
import socket


def get_domain(url):
    """Get domain name from url"""
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return domain


# print(get_domain("http://www.taiyuan.gov.cn/doc/2019/11/04/934354.shtml"))


class NetHelper:
    @staticmethod
    def get_domain(url):
        parsed_result = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_result)
        return domain

    @staticmethod
    def get_domain_url(url):
        """
        获取网址地址的域名url（区别于get_domain）
        :param url:
        :return:
        """
        parsed_uri = urlparse(url)
        domain_url = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return domain_url

    @staticmethod
    def get_ip(domain):
        addr = socket.getaddrinfo(domain, None)  # 'http'
        ip = addr[0][4][0]
        print(ip)
        return ip

    @staticmethod
    def get_ip_loc(ip):
        url = 'http://freeapi.ipip.net/'  # 中文免费
        url = url + format(ip)
        response = requests.get(url)

        res = response.text.replace('\"', '')  # 去掉双引号
        res = res.replace('[', '')  # 去掉方括号
        res = res.replace(']', '')
        res = res.replace(' ', '')

        res = res.split(",")  # 已逗号为分割符号，分割字符串为数组
        # print("****************************************")
        # print("您查询的IP地址 %s 来源地是：" % ip)
        # print("国家：%s" % (res[0]))  # 访问数组里面的值
        # print("省份：%s" % (res[1]))
        # print("城市：%s" % (res[2]))
        # print("区域：%s" % (res[3]))
        res[4] = res[4].replace('\n', '')  # 去掉回车符号
        # print("运营商：%s" % (res[4]))
        # print("数据来源<www.ipip.net免费查询接口>")
        return res

    @staticmethod
    def get_site_location(url):
        domain = NetHelper.get_domain(url)
        ip = NetHelper.get_ip(domain)
        location = NetHelper.get_ip_loc(ip)
        return location

    # USE: 用于提取URL各部分
    @staticmethod
    def parse_url(url, part=""):
        # http://www.example.com/a/b/index.php?id=1#h1
        # domain : www.example.com
        # scheme : http
        # path   : /a/b/index.php
        # id=1   : id=1
        # fragment : h1
        # completepath : /a/b/
        # completedomain : http://www.example.com
        # filename : index.php
        # filesuffix : php

        if not url.startswith("http"):
            if part == "path":
                return url[:url.rfind("/") + 1]
            if part == "filename":
                temp = url[url.rfind("/") + 1:]
                if temp.find("?") != -1:
                    temp = temp[:temp.find("?")]
                if temp.find("#") != -1:
                    temp = temp[:temp.find("#")]
                return temp
        else:
            pass
        try:
            parsed = urlparse(url)
        except Exception as e:
            # except ValueError as e:  # TODO: CHECK
            return ""
        if part == "domain":
            return parsed.netloc
        elif part == "scheme":
            return parsed.scheme
        elif part == "path":
            return parsed.path
        elif part == "query":
            return parsed.query
        elif part == "fragment":
            return parsed.fragment
        elif part == "completepath":
            return parsed.path[:parsed.path.rfind("/") + 1]
        elif part == "completedomain":
            return parsed.scheme + "://" + parsed.netloc
        elif part == "filename":
            return parsed.path[parsed.path.rfind("/") + 1:]
        elif part == "filesuffix":
            temp = parsed.path[parsed.path.rfind("/") + 1:]
            if temp.find(".") == -1: return ""
            return temp[temp.find("."):]
        else:
            return parsed
