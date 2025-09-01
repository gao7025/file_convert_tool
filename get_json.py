# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
from bs4 import BeautifulSoup
# from lxml import html
# import xml
# import requests


def get_data(url):
    data_json = url.get('sites', '')
    data_new = pd.DataFrame()
    for i in range(len(data_json)):
        # url = str(data.loc[i, 'output_result_path']).replace('-internal', '')
        # f = requests.get(url)  # Get该网页从而获取该html内容
        # soup = BeautifulSoup(f.content, "lxml")  # 与f.text功能一样，用lxml解析器解析该网页的内容
        # str_json = str(soup.body).strip('</p></body>')  # .replace('\t','').replace('\n','')
        # data_json = json.loads(str_json)
        data_new.loc[i, 'name'] = data_json[i].get('name', '')
        data_new.loc[i, 'url'] = data_json[i].get('url', '')

        print('we are done : ', i)
    print('result: \n', data_new)
    return data_new


if __name__ == '__main__':
    path = 'D:/py_program/get_json'
    fr3 = open(path + '/json_file.json', encoding='utf-8')
    json_file = json.load(fr3)
    get_data(json_file)

