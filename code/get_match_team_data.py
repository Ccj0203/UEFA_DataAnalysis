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

def get_match_team_data(id):
    print('正在获取比赛id为%s的比赛数据' % id)
    url = "https://matchstats.uefa.com/v1/team-statistics/%s" % id
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)

    return data #输出的是一个list，内含两个json

if __name__ == '__main__':
    # 获取比赛id
    match_ids = get_match_info()

    match_team_data = []
    for i in tqdm(match_ids):
        try:
            match_teams_data = get_match_team_data(i)
            match_team_data.append({
                'match_id':i,
                'match_team1_data':match_teams_data[0],
                'match_team2_data':match_teams_data[1],
            })
            time.sleep(0.5)
        except:
            print('请求失败，重新请求')
            time.sleep(3)
            match_team_data.append({
                'match_id':i,
                'match_team1_data':match_teams_data[0],
                'match_team2_data':match_teams_data[1],
            })
            time.sleep(0.5)  
    
    with open('data\\match_team_data.json','w',encoding='utf-8') as f:
        json.dump(match_team_data,f,ensure_ascii=False,indent=4)