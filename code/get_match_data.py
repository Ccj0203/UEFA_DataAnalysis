########################
# 运行时注意关闭科学上网！！#
########################

import pandas as pd
import json
import requests
from tqdm import *
import time
from get_match_info import get_match_info

headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

def get_match_data(id):
    url = "https://match.uefa.com/v5/matches?matchId=%s" % id
    res = requests.get(url,headers=headers)
    data = json.loads(res.text)[0]
    #   'id', 比赛id
    #   'awayTeam', 客场球队信息
    #       'id' 客场球队id
    #       'translation'
    #           'countryname'
    #               'ZH' 客场球队中文名称
    #   'homeTeam', 主场球队信息
    #       'id' 主场球队id
    #       'translation'
    #           'countryname'
    #               'ZH' 主场球队中文名称
    #   'score', 比分
    #       'regular' 常规时间比分
    #           'away' 客场球队得分
    #           'home' 主场球队得分
    #       'total' 全场比赛比分
    #           'away' 客场球队得分
    #           'home' 主场球队得分
    #   'playerOfTheMatch', 本场mvp球员
    #       'player'
    #           'translation'
    #               'name'
    #                   'ZH' 球员中文名
    #               'nationalFieldPosition'
    #                   'ZH' 球员位置（此项目中使用国家队位置）
    #   'playerEvents', 球员事件，红黄牌、进球等

    #   'behindClosedDoors', 非公开?不重要
    #   'competition', 比赛基本信息，比如成人组、男子、比赛类别（杯赛）等
    #   'fullTimeAt', 完赛时间
    #   'group', 组
    #   'kickOffTime', 比赛开始时间
    #   'lineupStatus',
    #   'matchAttendance',
    #   'matchNumber',
    #   'matchday', 比赛日信息
    #   'referees', 裁判信息
    #   'round', 系列赛阶段信息，小组赛、淘汰赛等
    #   'seasonYear', 
    #   'sessionNumber',
    #   'stadium', 球馆信息
    #   'status', 比赛状态
    #   'type', 小组赛？这个字段不确定
    #   'winner' 获胜球队

    need_match_data = [
        data['id'],
        data['awayTeam']['id'],
        data['awayTeam']['translations']['countryName']['ZH'],
        data['homeTeam']['id'],
        data['homeTeam']['translations']['countryName']['ZH'],
        data['score']['regular']['away'],
        data['score']['regular']['home'],
        data['score']['total']['away'],
        data['score']['total']['home'],
        data['playerOfTheMatch']['player']['translations']['name']['ZH'],
        data['playerOfTheMatch']['player']['translations']['nationalFieldPosition']['ZH'],
    ]
    return need_match_data


if __name__ == '__main__':
    # 获取比赛id
    match_ids = get_match_info()
    # print(match_ids)

    # match_data = get_match_data(2036161)
    match_data = []
    for i in tqdm(match_ids[:2]):
        match_data.append(get_match_data(i))
        time.sleep(0.5)
        
    columns = ['match_id',
                    'away_team_id',
                    'away_team_name',
                    'home_team_id',
                    'home_team_name',
                    'away_score',
                    'home_score',
                    'total_away_score',
                    'total_home_score',
                    'mvp_name',
                    'mvp_position']
    match_data = pd.DataFrame(match_data,columns=columns)
    # match_data.to_excel('.\\data\\match_data.xlsx',index=False)
    print(match_data)


