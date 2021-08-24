import json
import requests
import time

import os

from threading import Thread
from fastperfomance.settings import BASE_DIR

# 多线程装饰器
def acc(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)

        thr.start()

    return wrapper

#多线程调用os.system
@acc
def osrun(s):
    os.system(s)


class LocustFile(object):
    def __init__(self):
        self.name = 'locustfile'
    #把请求信息丢给对象
    def prepare_locust_tests(self, qjson):
        #请求信息转为字典
        body =eval(qjson['request'])
        self.name = body['name']
        self.url = body['request']['url']
        self.method = body['request']['method']
        self.threads = qjson['threads']
        self.rate = qjson['rate']
        self.execution_time = qjson['execution_time']
        self.assertstr = qjson['assertstr']
        self.path = qjson['path']
        self.type = 'Https'

        if 'params' in body['request']:
            params = body['request']['params']
            self.params = "?"
            for key in params:
                parm = key + "=" + params[key] + "&"

                self.params += parm
            self.params = self.params.rstrip("&")
            self.url = self.url + self.params
            # print(self.params)
        else:
            self.params = None

        if 'json' in body['request']:
            jsondict = json.dumps(body['request']['json'])
            self.json = "payload := strings.NewReader(`" + str(jsondict) + "`)"
            # print(self.json)
        else:
            self.json = None

        if 'data' in body['request']:
            datas = body['request']['data']
            self.data = ""
            for key in datas:
                data = key + "=" + datas[key] + "&"

                self.data += data
            # print(self.data)
            self.data = "payload := strings.NewReader(" + '"' + self.data.rstrip("&") + '"' + ")"
            # print(self.data)

        else:
            self.data = None

        if 'headers' in body['request']:
            self.headers = ""
            headers = body['request']['headers']
            for key in headers:
                header = "req.Header.Add(" + '"' + key + '"' + ',' + '"' + headers[key] + '"' + ')' + '\n'
                self.headers += header + '    '
            # print(self.headers)
        else:
            self.headers = None

        return self


def makefile(datatext):
    filename = BASE_DIR + '/templates/main.go'
    gofile = BASE_DIR + '/templates/' + 'main2.go'

    try:
        os.remove(gofile)
    except IOError:
        print('文件不存在')

    finally:
        fp = open(filename, 'r')
        content = fp.read()
        fp.close()

        c2 = content.replace('Url', '"%s"' % datatext.url, 1)
        c2 = c2.replace('Method', '"%s"' % datatext.method, 1)
        c2 = c2.replace('Rname', '"%s"' % datatext.name, 3)
        c2 = c2.replace('Assertstr', '"%s"' % datatext.assertstr, 1)
        c2 = c2.replace('Type', '"%s"' % datatext.type, 2)
        if datatext.headers != None:
            c2 = c2.replace('ReqHeader', datatext.headers, 1)
        else:
            c2 = c2.replace('ReqHeader', "")
        if datatext.data == None and datatext.json == None:
            print(datatext.data)
            print(datatext.json)
            c2 = c2.replace('Ipayload', 'nil')
        else:
            c2 = c2.replace('Ipayload', 'payload')
        if datatext.data != None:
            c2 = c2.replace('Payload', datatext.data)
        if datatext.json != None:
            c2 = c2.replace('Payload', datatext.json)
        # print(c2)
        f = open(gofile, 'w+')
        f.write(c2)
        read = f.readline()
        # print(read)
        f.close()
    return gofile


def run(parm):
    osrun('cd %s/templates/;go run %s.go' % (BASE_DIR, 'main2'))
    time.sleep(3)
    data = {'user_count': parm.threads,
            'spawn_rate': parm.rate}
    requests.post(url='http://0.0.0.0:8089/swarm', data=data)
    time.sleep(parm.execution_time)
    requests.get(url='http://0.0.0.0:8089/stop')
