import pandas as pd


def get_matches_data(path='./static/data/IPL Matches 2008-2020.csv'):
    data = pd.read_csv(path)

    # print(data.head())
    # print(data.describe())

    # # Check whether there are any null values present in the dataset.
    # print(data.isnull().sum())

    # # Look into the total teams listed in this dataset.
    # print(data["team1"].unique())

    # As there old names of some teams, changing the old name to the newer one.
    # for Delhi Capitals
    data['team1']=data['team1'].str.replace('Delhi Daredevils','Delhi Capitals')
    data['team2']=data['team2'].str.replace('Delhi Daredevils','Delhi Capitals')
    data['winner']=data['winner'].str.replace('Delhi Daredevils','Delhi Capitals')
    # for sunrisers Hyderabad
    data['team1']=data['team1'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
    data['team2']=data['team2'].str.replace('Deccan Chargers','Sunrisers Hyderabad')
    data['winner']=data['winner'].str.replace('Deccan Chargers','Sunrisers Hyderabad')

    return data


def get_teams(path='./static/data/teams.csv'):
    data = pd.read_csv(path)

    return data


def get_ball_by_ball(path='./static/data/ipl_scores.csv'):
    data = pd.read_csv(path)

    return data



if __name__ == '__main__':
    # print(get_matches_data())
    # print(get_teams())
    print(get_ball_by_ball())