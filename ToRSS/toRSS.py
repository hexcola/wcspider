#! /usr/bin/python 2.79 -Neo
# _*_ coding:utf-8 _*_

import time
import datetime
import requests
import json
import re
import xml.etree.ElementTree as ET
import os

#OPENID = 'oIWsFtyel13ZMva1qltQ3pfejlwU'
OPENID = 'oIWsFt67VuXqx-oTP8saLcpMxVLs'
XML_LIST = []

# get current time in milliseconds
current_milli_time = lambda: int(round(time.time() * 1000))

def get_json(pageIndex):
    global OPENID
    the_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Referer': 'http://weixin.sogou.com/gzh?openid={0}'.format(OPENID),
        'Host': 'weixin.sogou.com'
        }

    url = 'http://weixin.sogou.com/gzhjs?cb=sogou.weixin.gzhcb&openid={0}&page={1}&t={2}'.format(OPENID, pageIndex, current_milli_time())
    print(url)
    response = requests.get(url, headers = the_headers)

    # TO-DO; check if match the reg

    response_text = response.text

    #
    json_start = response_text.index('sogou.weixin.gzhcb(') + 19
    json_end = response_text.index('//<!--') - 2
    json_str = response_text[json_start : json_end]

    #print(json_str)

    # convert json_str to json object
    json_obj = json.loads(json_str)

    # print json_obj['totalPages']
    return json_obj


def add_xml(jsonObj):
    global XML_LIST
    xmls = jsonObj['items']
    #print type(xmls)
    XML_LIST.extend(xmls)



# ------------ Main ----------------
print 'play it :) '
# get total pages
default_json_obj = get_json(1)
total_pages = 0
total_items = 0

if(default_json_obj):
    # add the default xmls
    add_xml(default_json_obj)

    # get the rest items
    total_pages = default_json_obj['totalPages']
    total_items = default_json_obj['totalItems']
    print total_pages

    # iterate all pages
    if(total_pages >= 2):
        for pageIndex in range(2, total_pages + 1):
            add_xml(get_json(pageIndex))
            print 'load page ' + str(pageIndex)

    print len(XML_LIST)
