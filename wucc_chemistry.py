import requests
from bs4 import BeautifulSoup
import pandas as pd


############### GET LIST OF TEAMS ###############

def get_teams_from_rows(rows):
    teams = []
    for row in rows:
        x = row.find_all('td')
        if len(x) > 0:
            teams.append(x[0].text)
    return pd.Series(teams)

def list_of_teams():
    page_url = 'https://results.wfdf.sport/wucc/?view=teams&season=WUCC2022&list=allteams'
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')

    open_rows = tables[7].find_all('tr')
    open_teams = get_teams_from_rows(open_rows)
    
    womens_rows = tables[8].find_all('tr')
    womens_teams = get_teams_from_rows(womens_rows)

    mixed_rows = tables[9].find_all('tr')
    mixed_teams = get_teams_from_rows(mixed_rows)
    
    df = pd.concat([open_teams, womens_teams, mixed_teams], axis=1)
    df.columns = ['open teams', 'women\'s teams', 'mixed teams']
    df.to_csv('team_list.csv')

############### GET TEAM TOTAL GOALS ###############

def get_team_total(team_num):
    page_url = f'https://results.wfdf.sport/wucc/?view=teamcard&team={team_num}'
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')[7]
    name = ' '.join(soup.find('h1').text.split(' ')[:-1])

    rows = table.find_all('tr')
    total_goals = 0
    for row in rows:
        items = row.find_all('td')
        if len(items) > 3:
            total_goals += int(items[3].text)

    return name, total_goals

def get_all_team_totals():
    master_dict = dict()

    for i in range(1, 130):
        print(f'getting goals {i} of 129')
        name, goals = get_team_total(i)
        master_dict[name] = goals

    df = pd.DataFrame(list(zip(master_dict.keys(), master_dict.values())))
    df.columns = ['team', 'total goals']
    df.to_csv('team_goals.csv')

############### GET TEAM GIVEN PEOPLE ###############

def get_team(team1, team2, team1_table, team2_table, person1, person2):
    person1_names = person1.split()
    person2_names = person2.split()

    if len(person1_names) > 1:
        team1_check = all([person1_name in team1_table for person1_name in person1_names[1:]])
        if team1_check:
            return team1
        team2_check = all([person1_name in team2_table for person1_name in person1_names[1:]])
        if team2_check:
            return team2

    if len(person2_names) > 1:
        team1_check = all([person2_name in team1_table for person2_name in person2_names[1:]])
        if team1_check:
            return team1
        team2_check = all([person2_name in team2_table for person2_name in person2_names[1:]])
        if team2_check:
            return team2

    return "Unknown"

############### GET ENDZONE PAIRINGS ###############

def get_pairings(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    match = soup.find('h1').text.split('    ')[0].split(' - ')
    (team1, team2) = (match[0], match[1])
    tables = soup.find_all('table')
    rows = tables[-2].find_all('tr')

    team1_table = str(tables[7].find_all('table')[1])
    team2_table = str(tables[7].find_all('table')[3])

    pairings = []
    for row in rows:
        entries = row.find_all('td')
        
        if len(entries) >= 3:
            person1 = entries[1].text[:-1]
            person2 = entries[2].text[:-1]

            team = get_team(team1, team2, team1_table, team2_table, person1, person2)
            
            if person1 <= person2:
                pairings.append((person1, person2, team))
            else:
                pairings.append((person2, person1, team))

    return pairings

############### GET CSV OF POWER DUOS ###############

def generate_duos_csv():
    master_dict = dict()
    failed_games = []
    for i in range(1,653):
        print(f'working on {i} out of 652...')
        page_url = f'https://results.wfdf.sport/wucc/?view=gameplay&game={i}'
        try:
            pairings = get_pairings(page_url)
        except:
            pairings = []
        
        if len(pairings) == 0:
            failed_games.append(i)

        for pairing in pairings:
            master_dict[pairing] = master_dict.get(pairing, 0) + 1

    df = pd.Series(master_dict).reset_index()   
    df.columns = ['person 1', 'person 2', 'team', '# connections']
    df = df.sort_values(by='# connections', ascending=False)

    df.to_csv('wucc_duos.csv')
    print(failed_games)

############### MAIN ###############

if __name__ == '__main__':
    generate_duos_csv()
