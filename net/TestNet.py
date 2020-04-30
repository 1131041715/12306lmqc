import sys
sys.path.append("./")

from collections import OrderedDict

import collections
import random
import time
from http import cookiejar
from lxml import html
import requests
from define.UserAgent import USER_AGENT
from net import ips

import base64
from PIL import Image
import io

# ips = '36.6.146.162:9999'
def sendLogic(func):
    def wrapper(*args, **kw):
        for count in range(5):
            response = func(*args, **kw)
            if response is not None:
                return response
            else:
                time.sleep(0.1)
        return None

    return wrapper


class EasyHttp(object):
    __session = requests.Session()

    @staticmethod
    def get_session():
        return EasyHttp.__session

    @staticmethod
    def load_cookies(cookie_path):
        load_cookiejar = cookiejar.LWPCookieJar()
        load_cookiejar.load(cookie_path, ignore_discard=True, ignore_expires=True)
        load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)
        EasyHttp.__session.cookies = requests.utils.cookiejar_from_dict(load_cookies)

    @staticmethod
    def save_cookies(cookie_path):
        new_cookie_jar = cookiejar.LWPCookieJar(cookie_path)
        requests.utils.cookiejar_from_dict({c.name: c.value for c in EasyHttp.__session.cookies}, new_cookie_jar)
        new_cookie_jar.save(cookie_path, ignore_discard=True, ignore_expires=True)

    @staticmethod
    def updateHeaders(headers):
        EasyHttp.__session.headers.update(headers)

    @staticmethod
    def resetHeaders():
        EasyHttp.__session.headers.clear()
        EasyHttp.__session.headers.update({
            'User-Agent': random.choice(USER_AGENT), #FIREFOX_USER_AGENT
        })

    @staticmethod
    def setCookies(**kwargs):
        for k, v in kwargs.items():
            EasyHttp.__session.cookies.set(k, v)

    @staticmethod
    def removeCookies(key=None):
        EasyHttp.__session.cookies.set(key, None) if key else EasyHttp.__session.cookies.clear()

    @staticmethod
    @sendLogic
    def send(urlInfo, params=None, data=None, **kwargs):
        EasyHttp.resetHeaders()
        if 'headers' in urlInfo and urlInfo['headers']:
            EasyHttp.updateHeaders(urlInfo['headers'])
        try:
            if len(ips) == 0:
                response = EasyHttp.__session.request(method=urlInfo['method'],
                                                      url=urlInfo['url'],
                                                      params=params,
                                                      data=data,
                                                      timeout=3,
                                                      allow_redirects=False,
                                                      **kwargs)
            else:
                proxy_address = random.choice(ips)
                response = EasyHttp.__session.request(method=urlInfo['method'],
                                                      url=urlInfo['url'],
                                                      params=params,
                                                      data=data,
                                                      #python3发现proxies写成{"https": "https://{}"}的形式没法访问,笑哭-_-
                                                      proxies={"http": "http://{}".format(proxy_address[0])},
                                                      timeout=3,
                                                      allow_redirects=False,
                                                      **kwargs)
            if response.status_code == requests.codes.ok:
                if 'response' in urlInfo:
                    if urlInfo['response'] == 'binary':
                        return response.content
                    if urlInfo['response'] == 'html':
                        response.encoding = response.apparent_encoding
                        return response.text
                return response.json()
        except:
            if ips:
                ips.remove(proxy_address)
        return None

    @staticmethod
    @sendLogic
    def getHtmlTree(url, **kwargs):
        """
        获取html树
        """
        time.sleep(1)
        headers = {'Connection': 'keep-alive',
                  'Cache-Control': 'max-age=0',
                  'Upgrade-Insecure-Requests': '1',
                  'User-Agent': random.choice(USER_AGENT), #FIREFOX_USER_AGENT
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                  'Accept-Encoding': 'gzip, deflate, sdch',
                  'Accept-Language': 'zh-CN,zh;q=0.8',
                  }
        try:
            response = EasyHttp.__session.request(method='GET',
                                       url=url,
                                       # headers=headers,
                                       timeout=3,
                                       allow_redirects=False,
                                       **kwargs)
            if response.status_code == requests.codes.ok:
                return html.etree.HTML(response.text)
        except Exception as e:
            return None
        return None

    @staticmethod
    @sendLogic
    def get(url,timeout):
        try:
            if len(ips) == 0:
                response = EasyHttp.__session.request(method='GET',
                                                      url=url,
                                                      timeout=timeout,
                                                      allow_redirects=False)
            else:
                proxy_address = random.choice(ips)
                response = EasyHttp.__session.request(method='GET',
                                                      url=url,
                                                      proxies={"http": "http://{}".format(proxy_address[0])},
                                                      timeout=timeout,
                                                      allow_redirects=False)
            if response.status_code == requests.codes.ok:
                return response.text
        except Exception as e:
            return None
        return None

    @staticmethod
    @sendLogic
    def get_custom(urlInfo):
        try:
            if len(ips) == 0:
                response = EasyHttp.__session.request(method=urlInfo['method'],
                                                      url=urlInfo['url'],
                                                      timeout=3,
                                                      allow_redirects=False
                                                      )
            else:
                proxy_address = random.choice(ips)
                response = EasyHttp.__session.request(method=urlInfo['method'],
                                                      url=urlInfo['url'],
                                                      proxies={"http": "http://{}".format(proxy_address[0])},
                                                      timeout=3,
                                                      allow_redirects=False
                                                      )
        except Exception as e:
            if ips:
                ips.remove(proxy_address)
            return None
        return response

    @staticmethod
    @sendLogic
    def post_custom(urlInfo,data=None):
        EasyHttp.resetHeaders()
        if 'headers' in urlInfo and urlInfo['headers']:
            EasyHttp.updateHeaders(urlInfo['headers'])
        try:
            if len(ips) == 0:
                response = EasyHttp.__session.request(method=urlInfo['method'],
                                                      url=urlInfo['url'],
                                                      data=data,
                                                      timeout=3,
                                                      allow_redirects=False)
            else:
                proxy_address = random.choice(ips)
                response = EasyHttp.__session.request(method=urlInfo['method'],
                                                      url=urlInfo['url'],
                                                      data=data,
                                                      proxies={"http": "http://{}".format(proxy_address[0])},
                                                      timeout=3,
                                                      allow_redirects=False)
        except Exception as e:
            if ips:
                ips.remove(proxy_address)
            return None
        return response

if __name__ == '__main__':
    dic = collections.OrderedDict()
    dic['leftTicketDTO.train_date'] = '2019-01-01'
    dic['leftTicketDTO.from_station'] = 'SHH'
    dic['leftTicketDTO.to_station'] = 'GZQ'
    dic['purpose_codes'] = 'ADULT'
    # params = {
    #     r'leftTicketDTO.train_date': '2019-01-01',
    #     r'leftTicketDTO.from_station': 'SHH',
    #     r'leftTicketDTO.to_station': 'GZQ',
    #     r'purpose_codes': "ADULT"
    # }

    # headers = {"X-Requested-With": "XMLHttpRequest",
    #            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    #            "Accept-Encoding": "gzip, deflate, br",
    #            "Content-Type": "application/json;charset=utf-8"}
    # url = r'https://kyfw.12306.cn/otn/leftTicket/query' + "?leftTicketDTO.train_date=" + '2019-01-01' + "&leftTicketDTO.from_station=" + 'SHH' + "&leftTicketDTO.to_station=" + 'GZQ' + "&purpose_codes=ADULT"
    # result = requests.get(url,headers=headers,  timeout=15)
    # print("---------------------------------------------------------------------")
    # print(result.content)
    # print("---------------------------------------------------------------------")

    # urlInfoCodeImg = {
    #         "url": "https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&{0}".format(
    #             int(time.time() * 1000)),
    #         "method": "get"
    #     }
    # response = EasyHttp.send(urlInfoCodeImg)
    # if  not response is None:
    #         print('验证码图片有值',)
    #         img_base64 = base64.b64decode(response['image'])
 
    #         image = io.BytesIO(img_base64)
    #         img = Image.open(image)
    #         img.show()


    # urlInfoLog = {
    #         'url': r'https://kyfw.12306.cn/passport/web/login',
    #         'method': 'POST',
    #         'headers': {
    #             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #             'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
    #             'Accept': 'application/json, text/javascript, */*; q=0.01',
    #             'Origin': 'https://kyfw.12306.cn',
    #             'Host': 'kyfw.12306.cn'
    #         }
    #     }

    # payload = OrderedDict()
    # payload['username'] = '1131041715@qq.com'
    # payload['password'] = 'Any1131041715'
    # payload['appid'] = 'otn'

    # results = input("输入验证码索引(见上图，以','分割）: ")
    # payload['answer'] = results

    # response1 = EasyHttp.post_custom(urlInfoLog, data=payload)
    # print(response1.status_code)
    pass
