# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 14:55
# @Author  : JumpWater
import logging

import requests

SUCCESS = {
    'msg': 'success',
    'status': 0
}

FAILURE = {'msg': '未找到此条数据，请重新核对数据id', 'status': 1}


def debug_request(obj):
    data = eval(obj.request)['request']
    headers = ""

    try:

        if "headers" in str(data):
            headers = data['headers']

        if 'params' in str(data):
            res = requests.request(method=data['method'].lower(), url=data['url'], headers=headers,
                                   params=data['params']).json()
        elif 'json' in str(data):
            res = requests.request(method=data['method'].lower(), url=data['url'], headers=headers,
                                   json=data['json']).json()
        elif 'data' in str(data):
            res = requests.request(method=data['method'].lower(), url=data['url'], headers=headers,
                                   data=data['data']).json()
        else:
            res = requests.request(method=data['method'].lower(), url=data['url'], headers=headers).json()
        return res


    except Exception as e:
        print(e)
        return {'msg': '请求信息填写错误，请核对后再次尝试', 'status': 1}
