########################
# 运行时注意关闭科学上网！！#
########################

import json
import requests

headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

# 获取比赛id
def get_match_info():
    url = "https://match.uefa.com/v5/matches?competitionId=3&fromDate=2024-06-15&limit=55&offset=0&order=ASC&phase=ALL&seasonYear=2024&toDate=2024-07-14&utcOffset=8"
    
    print('开始爬取比赛id')
    res = requests.get(url,headers=headers)

    # 读取json数据
    data = json.loads(res.text)
    print('爬取比赛id完成')
    # 整理出比赛id
    return [i['id'] for i in data]

if __name__ == '__main__':
    print(get_match_info())
