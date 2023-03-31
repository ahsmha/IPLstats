import pickle
import numpy as np


FILE_NAME = './static/models/ipl_score_predict_model.pkl'
TEAMS = ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals''Royal Challengers Bangalore', 'Sunrisers Hyderabad']

def get_score(data):
    X_data = list()
    teams_temp = [0, 0, 0, 0, 0, 0, 0, 0]

    batting_team = data['batting_team']
    batting_index = TEAMS.index(batting_team)
    teams_temp[batting_index] = 1
    X_data += teams_temp
    teams_temp[batting_index] = 0

    bowling_team = data['bowling_team']
    bowling_index = TEAMS.index(bowling_team)
    teams_temp[bowling_index] = 1
    X_data += teams_temp
    teams_temp[batting_index] = 0

    
    overs = float(data['overs'])
    runs = int(data['runs'])
    wickets = int(data['wickets'])
    runs_in_prev_5 = int(data['runs_in_prev_5'])
    wickets_in_prev_5 = int(data['wickets_in_prev_5'])
    
    X_data = X_data + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
    X_data = np.array([X_data])
    model = pickle.load(open(FILE_NAME, 'rb'))
    result = model.predict(X_data)
    result = int(result[0])

    return result