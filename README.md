# 该方案已经失效

## 项目
使用爬虫搜索所有微信公众号资料及其文章

## 将特定公众号历史消息转换成RSS
1. 通过搜狗搜索获取公众号的openid
2. 创建公众号历史消息请求URL（http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid={0}&page={1}&t={2}）
3. 解析出历史消息总量、历史消息总页数、单个历史消息的XML
4. 根据读取到的所有的历史消息XML内容，创建RSS文件

## 参考
* http://www.pythonclub.org/python-network-application/observer-spider
* http://docs.seleniumhq.org/
* http://security.tencent.com/index.php/blog/msg/34
* http://www.zhihu.com/question/23643061
* http://scrapy.org/
* https://twistedmatrix.com/trac/
* http://www.yeeach.com/post/1210
* http://blog.csdn.net/ithomer/article/details/13999845
* http://www.zhihu.com/question/21405828
* http://weixin.sogou.com/gzh?openid=oIWsFtze5GMxNAYRhOFDGOXTTizw
* http://weixin.sogou.com/weixin
* http://it.sohu.com/20130627/n380077583.shtml
* http://segmentfault.com/q/1010000000714587
* http://www.zhihu.com/question/21288524
* http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid=oIWsFtze5GMxNAYRhOFDGOXTTizw&page=1&t=1411865005304
* http://www.oschina.net/question/2245966_173397
* http://www.zzzzy.com/201406103183.html
* https://github.com/omengye/spider/tree/master/pyspider
