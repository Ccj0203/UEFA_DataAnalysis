import json
import pandas as pd

if __name__ == '__main__':
    with open('..\\data\\match_team_data.json','r',encoding='utf-8') as f:
        js_match_team_data = json.load(f)

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
    
    pd.DataFrame(output, columns=['match_id', 'team_id', 'stat_name', 'stat_value', 'stat_unit', 'stat_trans']).to_excel('..\\data\\match_team_data.xlsx',index=False)
        

