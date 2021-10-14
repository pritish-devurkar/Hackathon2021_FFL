from espn_api.football import League

def analyzer(league_id, year, espn_s2, swid):

    league = League(league_id=league_id, year=year,espn_s2=espn_s2, swid=swid)

    top_scorer = league.player_map
    return top_scorer
#     adams_pts = league.player_info(name="Davante Adams")
    

#     print("Adams pts is..%s", adams_pts.projected_total_points)
#     print("Most points against %s", most_points_against)