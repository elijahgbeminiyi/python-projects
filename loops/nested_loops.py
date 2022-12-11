teams = ['Dragons', 'Wolves', 'Pandas', 'Falcons']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print("Team Home: {} | Team Away: {}".format(home_team, away_team))
