import json
import time
from threading import Thread

import gevent
import requests
def acc(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)

        thr.start()

    return wrapper
@acc
def requestThread(ctmp3):
    res1 = requests.post(url='http://127.0.0.1:8089/stop' + ctmp3)

    return res1.text

def makejson(qjson):
    body = eval(qjson['request'])
    transObj = {}
    transObj["isSession"] = 0 == 1
    transObj["HttpProxy"] = ""
    transObj["PreTask"] = None
    testTask = []
    xTestTask = {}
    xTestTask["TaskWeight"] = 1
    xTestTask["TaskName"] = body["name"]
    xTestTask["PreWork"] = None
    xTestTask["TestWork"] = makeHttpItem(body)
    testTask.append(xTestTask)
    transObj["MainTask"] = testTask
    return transObj


def makeHttpItem(body):
    xPretask = {}
    xPretask["Method"] = body['request']['method']
    xPretask["UrlPath"] = body['request']['url']
    if 'headers' in body['request']:
        xPretask["Headers"] = {}
        xPretask["Headers"] = body['request']['headers']
    else:
        xPretask["Headers"] = None
    if 'params' in body['request']:
        xPretask["Params"] = {}
        xPretask["Params"] = body['request']['params']
    else:
        xPretask["Params"] = None
    if 'data' in body['request']:
        xPretask["DictData"] = {}
        xPretask["DictData"] = body['request']['data']
    else:
        xPretask["DictData"] = None
    xPretask["RawData"] = ""
    if 'json' in body['request']:
        xPretask["JsonData"] = json.dumps(body['request']['json'])

    else:
        xPretask["JsonData"] = ""
    xPretask["AssertChain"] = [{
        "AssertType": 0,
        "RuleValue": 200
    }]
    xPretask["SaveParamChain"] = None
    return xPretask


def requestClient():
    response = requests.get(url='http://127.0.0.1:8089/stats/requests')
    res = response.text
    clent = json.loads(res)["slaves"]
    return clent


def initBoomer(host, json):
    host2 = ''
    for i in host:
        hostmp = i + '&'
        host2 += hostmp
    host3 = '?' + host2.rstrip('&')
    print(host3)
    try:
        response = requests.post(url='http://127.0.0.1:8089/initBoomer' + host3, json=json)
        return response
    except Exception as e:
        a = "无法连接locust服务器" + str(e)
        return a


def shotdownBoomer(host):
    host2 = ''
    for i in host:
        hostmp = i + '&'
        host2 += hostmp
    host3 = '?' + host2.rstrip('&')
    print(host3)
    try:
        response = requests.post(url='http://127.0.0.1:8089/shutdownBoomer' + host3)
        return response
    except Exception as e:
        a = "无法连接locust服务器" + str(e)
        return a


def swarm1(clients, user_count, hatch_rate, run_time,interface_id):
    data = {'user_count': user_count,
            'hatch_rate': hatch_rate}
    data2 = {'interface_id':interface_id}
    ctmp2 = ''
    for i in clients:
        ctmp = i + '&'
        ctmp2 += ctmp
    ctmp3 = '?' + ctmp2.rstrip('&')

    response = requests.post(url='http://127.0.0.1:8089/swarm' + ctmp3, data=data)
    time.sleep(int(run_time[0]))

    # res = requestThread(ctmp3)
    res1 = requests.post(url='http://127.0.0.1:8089/stop' + ctmp3,data=data2)
    print('1111222221111')
    print(res1)





    return res1
