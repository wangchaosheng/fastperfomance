# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 14:55
# @Author  : qingwu

import requests

SUCCESS = {
    'msg': 'success',
    'status': 0
}

FAILURE = {'status': 1}


def debug_request(obj):
    data = eval(obj.request)['request']
    try:
        if 'params' in str(data):
            res = requests.request(method=data['method'].lower(), url=data['url'], headers=data['headers'],
                                   params=data['params']).json()
        elif 'application/json' in str(data['headers']):
            res = requests.request(method=data['method'].lower(), url=data['url'], headers=data['headers'],
                                   json=data['json']).json()
        else:
            res = requests.request(method=data['method'].lower(), url=data['url'], headers=data['headers'],
                                   data=data['data']).json()
        return res
    except Exception:
        return {'msg': '请求信息填写错误，请核对后再次尝试', 'status': 1}
