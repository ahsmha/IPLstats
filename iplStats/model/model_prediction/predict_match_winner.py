import pickle
import pandas as pd


FILE_NAME = './static/models/ipl_match_win_predict_model.pkl'
TEAMS = ['Chennai Super Kings', 'Delhi Capitals', 'Gujarat Titans', 'Punjab Kings', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Lucknow Super Giants']


def get_match_winner(data):
    batting_team = data['batting_team']
    bowling_team = data['bowling_team']
    city = data['city']
    runs_left = data['runs_left']
    balls_left = data['balls_left']
    wickets_left = data['wickets_left']
    current_run_rate = data['current_run_rate']
    required_run_rate = data['required_run_rate']
    target = data['target']

    X_data = {
        'BattingTeam': batting_team,
        'BowlingTeam': bowling_team,
        'City': city,
        'runs_left': runs_left,
        'balls_left': balls_left,
        'wickets_left': wickets_left,
        'current_run_rate': current_run_rate,
        'required_run_rate': required_run_rate,
        'target': target
    }
    X_data = pd.DataFrame(data=X_data, index=[1])

    pipe = pickle.load(open(FILE_NAME, 'rb'))
    result = pipe.predict(X_data)

    return batting_team if result == 1 else bowling_team