# 侵权删除

# 只为个人研究学习，请合理使用工具，遵纪守法。

12306
=======
##### 鉴于2019年12306更新了抢票规则和候补策略，不管能不能帮助抢到票，都希望本工具能作为一个单点买票工具为大家在抢票思路上能做个参考

#### Usage
1. pip install -r requirements.txt安装所有依赖(Python3)

2. 在[configure.py]中配置信息：
 * 身份信息
 * 车票信息
 * 订票策略
 * 邮件配置
 * 短信配置
 * 线程池/进程池策略
 * IP池策略
 * 识别验证码策略

3. 执行[lmqceverything.py]
###### (ps:如果有登录验证失败次数过多,可以尝试自己抓deviceId Url来更新urls_conf.py文件中的getDevicesId对应的url。此外除了手动更改之外，可以替换train/login/Login.py中的_login_init方法中的self._handle_device_code_manual为self._handle_device_code_auto自动获取设备指纹。注：自动获取设备指纹方法容易引起12306拦截，请测试执行) DevicesId获取之前清除一下浏览器缓存。

##### 希望用工具抢到票的童鞋可以留个足迹，以资鼓励，发布地址:[issue](https://github.com/Any1131041715/12306lmqc/issues)

#### Notice
* 刷票频次最好不要太快，但是整点发售0.2秒最佳，网速不好，延迟大还真抢不过，哈哈
* IP池和登录方式酌情修改,短信发送twilio
* 配置详情请关注configure.py文件

#### 你可以做啥
* 要改成多线程多进程随你咯
* 添加自己的代理池随你咯
* 添加多账户支持随你咯
* 方便个人，不为盈利

###### 提示
* 借鉴了[V-I-C-T-O-R](https://github.com/V-I-C-T-O-R/12306)的代码
* 借鉴了[EasyTrain](https://github.com/Why8n/EasyTrain "EasyTrain")库的代码
* 借鉴了[proxy_pool](https://github.com/jhao104/proxy_pool "proxy_pool")库的代码
* 借鉴了其他开源代码
* 优化当前代码和流程



