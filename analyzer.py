from espn_api.football import League, Player

def player_lists(league_id, year, espn_s2, swid):

    league = League(league_id=league_id, year=year,espn_s2=espn_s2, swid=swid)

    # players = league.player_map
    # # first_player = next(iter(players.items()))
    # playerList = list(players.keys())
    # playerIds = playerList[::2]
    # playerNamesStr = get_player_names(playerList)
    # for key in players.keys():
    #     playertuple = key
    #     #playertuple1 = val(0)
    #     playerNames = playertuple
    #     print(type(playertuple))
    #     #print(playertuple1)
    # print(playerList)
    allrosteredplayers = []
    for team in league.teams:
        for player in team.roster:
            allrosteredplayers.append(player)

    # for arp in allrosteredplayers:
    #     print(arp.name)
    
    # print(len(allrosteredplayers))

    # print(allplayers)

    # print("Such a long list...")
    # print(len(playerList))
    # playernames = players.get(1)
    # print(playernames)
    return allrosteredplayers

def get_player_names(values):
    player_names = []
    for index in range(1, len(values), 2):
        player_names.append(values[index])

    # print(player_names)
    # print(len(player_names))
    return player_names
#     adams_pts = league.player_info(name="Davante Adams")
    

#     print("Adams pts is..%s", adams_pts.projected_total_points)
#     print("Most points against %s", most_points_against)