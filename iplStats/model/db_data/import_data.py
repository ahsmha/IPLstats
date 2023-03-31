import sqlite3
import pandas as pd
from get_data import get_teams


CONNECTION = sqlite3.connect('./db.sqlite3')
CURSOR = CONNECTION.cursor()

def import_teams():
    try:
        teams = get_teams('./static/data/dataset_1/Teams.csv')
        teams.to_sql('teams', CONNECTION, if_exists='append', index = False)
    except Exception as ex:
        print('[Error][import_data:import_teams]: ', ex)
        return False
    else: return True
    

def get_all_rows(table):
    try:
        output = CURSOR.execute(f'''SELECT * FROM {table}''').fetchall()
    except Exception as ex:
        print('[ERROR][import_data:get_all_rows]: ', ex)
        return None
    else: return output


def remove_all_rows(table):
    try:
        CURSOR.execute(f'''DELETE FROM {table}''')
        CONNECTION.commit()
    except Exception as ex:
        print('[ERROR][import_data:remove_all_data]: ', ex)
        return False
    else: return True


def remove_table(table):
    try:
        CURSOR.execute(f'''DROP TABLE {table}''')
        CONNECTION.commit()
    except Exception as ex:
        print('[ERROR][import_data:remove_table]: ', ex)
        return False
    else: return True


if __name__ == '__main__':
    # print(import_teams())
    # print(remove_table('teams'))
    print('output>>>', get_all_rows('teams'))
    # print('remove>>>>', remove_all_rows('teams'))
