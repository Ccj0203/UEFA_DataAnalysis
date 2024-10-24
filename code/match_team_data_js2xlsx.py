import json
import pandas as pd
import os

def json_to_long(json_text):

    js_match_team_data = json_text

    output = []
    for match in js_match_team_data:
        match_id = match['match_id']
        for team in ['match_team1_data', 'match_team2_data']:
            team_data = match[team]
            team_id = team_data['teamId']
            for stat in team_data['statistics']:
                stat_name = stat['name']
                stat_value = stat['value']
                try:
                    stat_unit = stat['unit']
                except KeyError:
                    stat_unit = ''

                try:    
                    stat_trans = stat['translations']['name']['EN']
                except KeyError:
                    stat_trans = ''
                output.append([match_id, team_id, stat_name, stat_value, stat_unit, stat_trans])
    
    return pd.DataFrame(output, columns=['match_id', 'team_id', 'stat_name', 'stat_value', 'stat_unit', 'stat_trans'])
    

if __name__ == '__main__':
    print(os.getcwd())
    with open('data\\match_team_data.json','r',encoding='utf-8') as f:
        js_match_team_data = json.load(f)

    match_team_data_long = json_to_long(js_match_team_data)
    match_team_data_long.to_excel('data\\match_team_data_LONG.xlsx',index=False)
    # match_team_data_long.to_excel('..\\data\\match_team_data_LONG.xlsx',index=False)

    match_team_data_wide = match_team_data_long.pivot(index=['match_id', 'team_id'], columns='stat_name', values='stat_value')
    match_team_data_wide.to_excel('data\\match_team_data_WIDE.xlsx',index=True)
    # match_team_data_wide.to_excel('..\\data\\match_team_data_WIDE.xlsx',index=True)


