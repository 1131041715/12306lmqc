import random
import time

loginUrls = {
    'normal': {
        'index': {
            'url': r'https://www.12306.cn/index/',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1',
            },
            'response': 'html',
        },
        'conf': {
            'url': 'https://kyfw.12306.cn/otn/login/conf',
            'method': 'POST',
            'response': 'html',
        },
        'init': {
            'url': r'https://kyfw.12306.cn/otn/login/init',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
            },
            'response': 'html',
        },
        'loginInit': {
            'url': r'https://kyfw.12306.cn/otn/resources/login.html',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Referer': r'https://www.12306.cn/index/',
                'Upgrade-Insecure-Requests': '1',
                'Accept-Encoding': 'gzip, deflate, br',
            },
            'response': 'html',
        },
        'uamtk': {
            'url': r'https://kyfw.12306.cn/passport/web/auth/uamtk',
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': r'application/json, text/javascript, */*; q=0.01',
                'Origin':'https://kyfw.12306.cn'
            }
        },
        'uamtk-static': {
            'url': r'https://kyfw.12306.cn/passport/web/auth/uamtk-static',
            'method': 'POST',
            'headers': {
                r'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
            }
        },
        'captcha': {
            'url': r'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&{}'
                .format(random.random()),
            'method': 'GET',
            'response': 'binary',
            'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
        },
        "loginCaptchaCode": {
            "url": "https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&{0}".format(
                int(time.time() * 1000)),
            "method": "get"
        },
        'captchaCheck': {
            'url': r'https://kyfw.12306.cn/passport/captcha/captcha-check',
            'method': 'GET',
            'headers': {
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
            }
        },
        'login': {
            'url': r'https://kyfw.12306.cn/passport/web/login',
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'https://kyfw.12306.cn',
                'Host': 'kyfw.12306.cn'
            }
        },
        'userLogin': {
            'url': r'https://kyfw.12306.cn/otn/login/userLogin',
            'method': 'GET',
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
                'Upgrade-Insecure-Requests': '1',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            },
            'response': 'html',
        },
        'userLoginRedirect': {
            'url': r'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
            'method': 'GET',
            'headers': {
                'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
                'Upgrade-Insecure-Requests': '1',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            },
            'response': 'html'
        },
        'uamauthclient': {
            'url': r'https://kyfw.12306.cn/otn/uamauthclient',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
            }
        },
        'checkUser': {
            'url': r'https://kyfw.12306.cn/otn/login/checkUser',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
            }
        },
        'loginOut': {
            'url': r'https://kyfw.12306.cn/otn/login/loginOut',
            'method': 'GET',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/index/initMy12306',
            },
            'response': 'html',
        },
        "getDevicesId": {  # 获取用户信息
            "url": r"https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=RXMn0n8yEh&hashCode=iz8vio-3Lji8F4W2Tsatbx25NzJ8KCD9-ZYeZEEzP9Y&FMQw=0&q4f3=zh-cn&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=1&EOQP=c227b88b01f5c513710d4b9f16a5ce52&jp76=8496cc0b1f00444d539d1f53e6c5d4af&hAqN=MacIntel&platform=WEB&ks0Q=e848b8c6800147e416e6663782ca3789&TeRS=777x1280&tOHY=24xx800x1280&Fvje=i1l1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_14_6)%20AppleWebKit/605.1.15%20(KHTML,%20like%20Gecko)%20Version/13.1%20Safari/605.1.15&E3gR=67d748ae63cb0351537c34d1133960d0&timestamp=",
            # "url": "https://kyfw.12306.cn/otn/HttpZF/logdevice",
            "method": "GET",
            'response': 'html',
            'headers': {
                'Host': 'kyfw.12306.cn',
                # 'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0',
            }
        },
        "getJS": {
            "url": "https://kyfw.12306.cn/otn/HttpZF/GetJS",
            "method": "GET",
            'response': 'html',
            'headers': {
                "Referer": "https://kyfw.12306.cn/otn/confirmPassenger/initDc",
                'Host': 'kyfw.12306.cn',
            }
        }
    }
}

autoVerifyUrls = {
    '12305': {
        'url': 'https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&{0}'.format(
            int(time.time() * 1000)),
        'method': 'GET',
        # 'response': 'html',
    },
    'api': {
        'url': 'https://12306.jiedanba.cn/api/v2/getCheck',
        'method': 'POST',
        'headers': {'Content-Type': 'application/json'}
    },
    'img_url': {
        'url': 'https://check.huochepiao.360.cn/img_vcode',
        'method': 'POST'
    },
    'check_url': {
        'url': 'https://kyfw.12306.cn/passport/captcha/captcha-check',
        'method': 'GET'
    },
    "origin_url": "https://12306.jiedanba.cn/"
}

queryUrls = {
    'query': {
        'url': r'https://kyfw.12306.cn/otn/leftTicket/query',
        'method': 'GET',
        'headers': {
            'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
        }
    },
}
submitUrls = {
    'dc': {
        'submitOrderRequest': {
            'url': r'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest',
            'method': 'POST',
            'headers': {
                'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': r'kyfw.12306.cn',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Origin': 'https://kyfw.12306.cn',
            },
        },
        'getPassengerDTOs': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs',
            'method': 'POST',
        },
        'getExtraInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            'method': 'POST',
            'headers': {
                'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
                'Host': r'kyfw.12306.cn',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0',
            },
            'response': 'html',
        },
        'checkUser': {
            'url': r'https://kyfw.12306.cn/otn/login/checkUser',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
            }
        },
        'checkOrderInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'getQueueCount': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'confirmForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
        },
        'queryOrderWaitTime': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime',
            'method': 'GET',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'resultOrderForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'queryMyOrderNoComplete': {
            'url': r'https://kyfw.12306.cn/otn/queryOrder/queryMyOrderNoComplete',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/queryOrder/initNoComplete',
            },
        }

    },
    'wc': {
        'submitOrderRequest': {
            'url': r'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest',
            'method': 'POST',
            'headers': {
                'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': r'kyfw.12306.cn',
                'X-Requested-With': 'XMLHttpRequest'
            },
        },
        'getPassengerDTOs': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs',
            'method': 'POST',
        },
        'getExtraInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            'method': 'GET',
            'response': 'html',
        },
        'checkOrderInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'checkUser': {
            'url': r'https://kyfw.12306.cn/otn/login/checkUser',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
            }
        },
        'getQueueCount': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'confirmForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/confirmGoForQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
        },
        'queryOrderWaitTime': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime',
            'method': 'GET',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'resultOrderForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForWcQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'queryMyOrderNoComplete': {
            'url': r'https://kyfw.12306.cn/otn/queryOrder/queryMyOrderNoComplete',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/queryOrder/initNoComplete',
            },
        }

    }
}

tencent_api = {
    # 基本文本分析API
    "nlp_wordseg": {
        'APINAME': '分词',
        'APIDESC': '对文本进行智能分词识别，支持基础词与混排词粒度',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordseg',
        'APIPARA': 'text'
    },
    "nlp_wordpos": {
        'APINAME': '词性标注',
        'APIDESC': '对文本进行分词，同时为每个分词标注正确的词性',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordpos',
        'APIPARA': 'text'
    },
    'nlp_wordner': {
        'APINAME': '专有名词识别',
        'APIDESC': '对文本进行专有名词的分词识别，找出文本中的专有名词',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordner',
        'APIPARA': 'text'
    },
    'nlp_wordsyn': {
        'APINAME': '同义词识别',
        'APIDESC': '识别文本中存在同义词的分词，并返回相应的同义词',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordsyn',
        'APIPARA': 'text'
    },

    # 计算机视觉--OCR识别API
    "ocr_generalocr": {
        'APINAME': '通用OCR识别',
        'APIDESC': '识别上传图像上面的字段信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr',
        'APIPARA': 'image'
    },
    "ocr_handwritingocr": {
        'APINAME': '手写OCR识别',
        'APIDESC': '识别上传图像上面的字段信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_handwritingocr',
        'APIPARA': 'image'
    },
    "ocr_idcardocr": {
        'APINAME': '身份证OCR识别',
        'APIDESC': '识别身份证图像上面的详细身份信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_idcardocr',
        'APIPARA': 'image,card_type'
    },
    "ocr_bcocr": {
        'APINAME': '名片OCR识别',
        'APIDESC': '识别名片图像上面的字段信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_bcocr',
        'APIPARA': 'image'
    },
    "ocr_driverlicenseocr": {
        'APINAME': '行驶证驾驶证OCR识别',
        'APIDESC': '识别行驶证或驾驶证图像上面的字段信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_driverlicenseocr',
        'APIPARA': 'image,type'
    },
    "ocr_bizlicenseocr": {
        'APINAME': '营业执照OCR识别',
        'APIDESC': '识别营业执照上面的字段信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_bizlicenseocr',
        'APIPARA': 'image'
    },
    "ocr_creditcardocr": {
        'APINAME': '银行卡OCR识别',
        'APIDESC': '识别银行卡上面的字段信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_creditcardocr',
        'APIPARA': 'image'
    },
    # 物体识别--OCR识别API
    "vision_objectr": {
        'APINAME': '物体OCR识别',
        'APIDESC': '对图片进行物体识别，快速找出图片中包含的物体信息',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/vision/vision_objectr',
        'APIPARA': 'image',
        'TENCENT_ENTITY_URL': 'https://ai.qq.com/doc/vision_object.shtml'
    },
    "image_tag": {
        'APINAME': '多标签识别',
        'APIDESC': '识别一个图像的标签信息,对图像分类',
        'APIURL': 'https://api.ai.qq.com/fcgi-bin/image/image_tag',
        'APIPARA': 'image'
    },
}
