########################
# 运行时注意关闭科学上网！！#
########################

import json
import requests
from tqdm import *
import time
from get_match_info import get_match_info
from random_user_agent import random_user_agent

headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent':random_user_agent()
}

def get_match_data(id):
    print('正在获取比赛id为%s的比赛数据' % id)
    url = "https://match.uefa.com/v5/matches?matchId=%s" % id
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)[0]

    return data #输出的是json


if __name__ == '__main__':
    # 获取比赛id
    match_ids = get_match_info()
    # print(match_ids)

    # match_data = get_match_data(2036161)
    match_data = []
    for i in tqdm(match_ids):
        try:
            match_data.append(get_match_data(i))
            time.sleep(0.5)
        except:
            print('请求失败，重新请求')
            time.sleep(3)
            match_data.append(get_match_data(i))
            time.sleep(0.5)
        
    with open('data\\match_data.json','w',encoding='utf-8') as f:
        json.dump(match_data,f,ensure_ascii=False,indent=4)
    # print(match_data)


