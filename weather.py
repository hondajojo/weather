#!/usr/bin/env python2
#-*- coding=utf-8 -*-
import urllib
def getdic(url):
    page = urllib.urlopen(url).read()

    pro_split = page.split(',')
    dic = {}
    for i in pro_split:
        i_split = i.split('|')
        dic[i_split[0]]=i_split[1]
    return dic

def get_pro(url):
    pro_dic = getdic(url)
    return pro_dic

def get_city(url):
    city_dic = getdic(url)
    return city_dic

def get_field(url):
    field_dic = getdic(url)
    return field_dic
if __name__ == '__main__':
    city_code_file = open('city.py','w')
    city_code_file.write('# -*- coding:utf-8 -*-\n')
    city_code_file.write('city = {}\n')
    print '获取省或直辖市编号'
    pro_dic=get_pro('http://m.weather.com.cn/data5/city.xml')
    print '获取二级区域编号'
    for pro in pro_dic:
        city_url = 'http://m.weather.com.cn/data5/city'+pro+'.xml'
        city_dic = get_city(city_url)
        for city in city_dic:
            field_url = 'http://m.weather.com.cn/data5/city'+city+'.xml'
            field_dic = getdic(field_url)
            for field in field_dic:
                city_code_file.write('city[\''+field_dic[field]+'\']='+'101'+str(field)+'\n')
city_code_file.close()
print 'done'


