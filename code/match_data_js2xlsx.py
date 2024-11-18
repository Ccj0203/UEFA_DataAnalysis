# 这份文档为match_data.json数据的转换，包含了match_data以及event和referee的数据
import json
import pandas as pd

def match_data_json_to_wide(json_text):

    js_match_data = json_text

    output = []
    for match in js_match_data:
        
        match_id = match['id']
        match_competiton_name = match['competition']['translations']['name']['EN']
        match_competiton_type = match['competition']['type'] 
        match_round_name = match['round']['translations']['name']['EN']
        match_isBehindClosedDoors = match['behindClosedDoors']
        match_homeTeam_name = match['homeTeam']['translations']['countryName']['EN']
        match_homeTeam_id = match['homeTeam']['id']
        match_awayTeam_name = match['awayTeam']['translations']['countryName']['EN']
        match_awayTeam_id = match['awayTeam']['id']
        match_score_regular_home = match['score']['regular']['home']
        match_score_regular_away = match['score']['regular']['away']
        match_score_total_home = match['score']['total']['home']
        match_score_total_away = match['score']['total']['away']
        
        try:
            match_score_penalty_home = match['score']['penalty']['home'] # 这俩要try一下
            match_score_penalty_away = match['score']['penalty']['away'] # 这俩要try一下
        except KeyError:
            match_score_penalty_home = ''
            match_score_penalty_away = ''
        
        try:
            match_winner_name = match['winner']['match']['team']['translations']['countryName']['EN']
        except KeyError:
            match_winner_name = match['winner']['match']['reason']
        match_playerOfTheMatch = match['playerOfTheMatch']['player']['translations']['name']['EN']
        
        index_lst = [match_id,
                        match_competiton_name, 
                        match_competiton_type,
                        match_round_name,
                        match_isBehindClosedDoors,
                        match_homeTeam_name,
                        match_homeTeam_id,
                        match_awayTeam_name,
                        match_awayTeam_id,
                        match_score_regular_home,
                        match_score_regular_away,
                        match_score_total_home,
                        match_score_total_away,
                        match_score_penalty_home,
                        match_score_penalty_away,
                        match_winner_name,
                        match_playerOfTheMatch
                        ]

        output.append(index_lst)
    
    return pd.DataFrame(output, 
                                columns=['match_id',
                                    'match_competiton_name', 
                                    'match_competiton_type',
                                    'match_round_name',
                                    'match_isBehindClosedDoors',
                                    'match_homeTeam_name',
                                    'match_homeTeam_id',
                                    'match_awayTeam_name',
                                    'match_awayTeam_id',
                                    'match_score_regular_home',
                                    'match_score_regular_away',
                                    'match_score_total_home',
                                    'match_score_total_away',
                                    'match_score_penalty_home',
                                    'match_score_penalty_away',
                                    'match_winner_name',
                                    'match_playerOfTheMatch'
                                ])

def event_data_json_to_long(json_text):

    js_match_data = json_text

    output = []
    for match in js_match_data:
        match_id = match['id']
        for index in ['scorers', 'redCards', 'penaltyScorers', 'penaltiesMissed']:
            try:
                for event in match['playerEvents'][index]:
                    player_name = event['player']['translations']['name']['EN']
                    player_position = event['player']['translations']['fieldPosition']['EN']
                    event_time_minute = event['time']['minute']
                    event_time_second = event['time']['second']
                    event_time = f'{event_time_minute:02d}:{event_time_second:02d}'
                    # print(f'[{match_id}] {index} : {player_name} ({player_position}) - {event_time_minute:02d}:{event_time_second:02d}')
                    output.append([match_id, index, player_name, player_position, event_time])
            except KeyError:
                pass
    
    return pd.DataFrame(output, columns=['match_id', 'event_type', 'player_name', 'player_position', 'event_time'])

def referee_data_json_to_long(json_text):

    js_match_data = json_text

    output = []

    for match in js_match_data:
        match_id = match['id']
        for ref in match['referees']:
            ref_name = ref['person']['translations']['name']['EN']
            try:
                ref_country = ref['person']['translations']['countryName']['EN']
            except KeyError:
                ref_country = 'Unknown'
            ref_role = '_'.join([i.capitalize() for i in ref['role'].split('_')])
            output.append([match_id, ref_name, ref_country, ref_role])
            # print(f'[{match_id}] Referee: {ref_name} ({ref_country}) - {ref_role}')
    
    return pd.DataFrame(output, columns=['match_id', 'ref_name', 'ref_country', 'ref_role'])

def get_team_dict(df_wide):
    home_team_all = df_wide[['match_homeTeam_id', 'match_homeTeam_name']].drop_duplicates()
    home_team_all.columns = ['team_id', 'team_name']
    away_team_all = df_wide[['match_awayTeam_id', 'match_awayTeam_name']].drop_duplicates()
    away_team_all.columns = ['team_id', 'team_name']
    return pd.concat([home_team_all, away_team_all]).drop_duplicates()


if __name__ == '__main__':

    # .py的工作路径是整个project的根目录，读取数据文件直接进入data目录
    with open('data\\match_data.json', 'r', encoding='utf-8') as f:
        js_match_data = json.load(f)

    match_data_wide = match_data_json_to_wide(js_match_data)
    match_data_wide.to_excel('data\\match_data_WIDE.xlsx', index=False)

    event_data_long = event_data_json_to_long(js_match_data)
    event_data_long.to_excel('data\\event_data_LONG.xlsx', index=False)

    referee_data_long = referee_data_json_to_long(js_match_data)
    referee_data_long.to_excel('data\\referee_data_LONG.xlsx', index=False)

    # 利用match_data_wide整理一份球队id和球队名称的字典表
    team_all = get_team_dict(match_data_wide)
    team_all.to_excel('data\\team_dict.xlsx', index=False)