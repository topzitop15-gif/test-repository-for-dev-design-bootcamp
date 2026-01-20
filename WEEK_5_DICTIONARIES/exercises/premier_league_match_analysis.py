#Premier League Match Analysis

#You're a Data Analyst at a sport analytics company (like Opta sports, Sofascore)
#Your job is to anlalyse match statistics to provide insights for punters, team managers, sports journalists, amd fantasy football players
#You are required to analyse goal scoring patterns from the latest game week.

#Sport analytics companies use analytics techniques to power platforms like FPL, betting odds, tactical analysis

#The Problem
#We have a goal data from 10 premier league matches in a game week, and required to :
#1.Count how many goals each team scored
#2.Find the highest scoring teams and matches
#3.Calculate goal statistics (average goal per match, most prolific teams)
#4.Identify teams in good form vs struggling teams




gameweek_matches =[
    {"match_id" : 1, "home_team": "Arsenal", "away_team": "Brighton",
     "home_goals": 3, "away_goals": 0, "venue":"Emirates Stadium"},

     {"match_id" : 2, "home_team": "Liverpool", "away_team": "Bournemouth",
     "home_goals": 4, "away_goals": 1, "venue":"Anfield"},

     {"match_id" : 3, "home_team": "Man City", "away_team": "Everton",
     "home_goals": 2, "away_goals": 1, "venue":"Etihad Stadium"},

     {"match_id" : 4, "home_team": "Chelsea", "away_team": "Wolves",
     "home_goals": 3, "away_goals": 1, "venue":"Stamford bridge"},

     {"match_id" : 5, "home_team": "Newcastle", "away_team": "Fulham",
     "home_goals": 2, "away_goals": 2, "venue":"St James' Park"},

     {"match_id" : 6, "home_team": "Aston Villa", "away_team": "Man United",
     "home_goals": 1, "away_goals": 2, "venue":"Villa Park"},

     {"match_id" : 7, "home_team": "Tottenham", "away_team": "Brentford",
     "home_goals": 2, "away_goals": 2, "venue":"Tottenham Hotspur Stadium"},

     {"match_id" : 8, "home_team": "West Ham", "away_team": "Crystal Palace",
     "home_goals": 0, "away_goals": 1, "venue":"Emirates Stadium"},

     {"match_id" : 9, "home_team": "Nottingham Forest", "away_team": "Sheffield",
     "home_goals": 1, "away_goals": 0, "venue":"City Ground"},

     {"match_id" : 10, "home_team": "Luton Town", "away_team": "Burnley",
     "home_goals": 1, "away_goals": 1, "venue":"Kenilworth Road"},
]

from pprint import pprint


print("\n" + "="* 50)
print("""
      PREMIER LEAGUE GAMEWEEK 10 ANALYSIS

      AUTHOR :TEMITOPE OLUGBAMILA
      
      """)
print("="* 50)


#step1:Extract Goal Per Team
#Concept:Process a list of dictionaries to aggregate team statistics

team_goals= {}

for match in gameweek_matches:
    #Extract match data
    home_team=match["home_team"]
    away_team=match["away_team"]
    home_goals=match["home_goals"]
    away_goals=match["away_goals"]

    #Get goals for the home team
    team_goals[home_team] = home_goals

    #Get goals for the away team
    team_goals[away_team] = away_goals

print("Team Goals")
pprint (team_goals)
print("")

print("\n Goals Scored By Team:")
for (team,goals) in team_goals.items():
    print(f"    {team}: {goals} goal(s)")

#step 2:a-Highest scoring team
goal_threshold = 3
highest_scoring_teams = {}

for(team, goals) in team_goals.items():
    if goals >= goal_threshold:
        highest_scoring_teams[team]= goals


print("\n  Highest scoring Teams:")
pprint(highest_scoring_teams)

#step 2b:Highest Scoring Matches
match_goals_threshold= 4
highest_scoring_matches = []

for match in gameweek_matches:
    home_goals=match["home_goals"]
    away_goals=match["away_goals"]

    if (home_goals+away_goals) >= match_goals_threshold:
        __match = match.copy()
        del __match["venue"]
        del __match["match_id"]

        highest_scoring_matches.append(__match)
        


print("\n Highest scoring Matches:")  
pprint(highest_scoring_matches) 

#TO DO:Display highest scoring matching and highest scoring team 

#step3:Average goals per match
print("\n Match Statistics:")

total_goals = sum(team_goals.values())
Avg_goals_per_match=sum(team_goals.values()) / len(gameweek_matches)

print(f"  Avg Goals Per Game: {Avg_goals_per_match}")
print(f"  Most Prolific Team: {", ".join(highest_scoring_teams.keys())}") #delimeter
print("")

for match in gameweek_matches:
    home = match["home_team"]
    away = match["away_team"]
    home_goals = match["home_goals"]
    away_goals= match["away_goals"]

    total_match_goals= home_goals + away_goals

    #Display match result
    if home_goals > away_goals:
        result = f"✓(home) WIN"
    elif away_goals > home_goals:
        result = f"✓(away) WIN"    
    else:
        result = f"🤝 Draw"    

    

    #Determine entertainment rating
    if total_match_goals >= 5:
        entertainment = " 🔥THRILLER"
    elif total_match_goals >= 3:
        entertainment = "😃Exciting"
    elif total_match_goals == 0:
        entertainment = "😴Boring"
    else:
        entertainment = "✓Decent"

    print(f"\n {home} {home_goals} - {away_goals} {away}")
    print(f"    {result} | {total_match_goals} goals | {entertainment}")
    print(f"    Venue: {match["venue"]}")


#step4: Team classification
print("\n Team From CLassification:") 

#Classification
#Excellent form is for teams that score 3+ goals
#Good form is for team that score 2 goals
#Average form is for teams that score 1 goal
#Poor form is for teams that score 0 goal

#Struggling teams = teams in average and poor form
#Good teams = teams in good and excellent form 

excellent_form={}
good_form={}
average_form={}
poor_form={}

for (__team, __goals) in team_goals.items():
    if __goals >= 3:
        #team is in excellent form
        excellent_form[__team] = __goals
    elif __goals == 2:
        #team is in good form
        good_form[__team] = __goals
    elif __goals == 1:
        #team is in average form
        average_form[__team] = __goals 
    else:
        #team is in poor form
        poor_form[__team] = __goals 

print(f"\n Excellent Form (3+ goals): {len(excellent_form)} teams")
for(__team,__goals) in excellent_form.items():
    print(f"    {__team}: {__goals} goals -Title contenders")

print(f"\n Good Form (3+ goals): {len(good_form)} teams")
for(__team,__goals) in good_form.items():
    print(f"    {__team}: {__goals} goals -Solid Attack")

print(f"\n Average Form (3+ goals): {len(average_form)} teams")
for(__team,__goals) in average_form.items():
    print(f"    {__team}: {__goals} goals -Need Improvement")

print(f"\n Poor Form (3+ goals): {len(poor_form)} teams")
for(__team,__goals) in poor_form.items():
    print(f"    {__team}: {__goals} goals -Major Concern")    


#Performance summary
scoring_teams =len(excellent_form)+len(good_form)+len(average_form)
scoring_rate = (scoring_teams / total_goals) * 100

print(f"\n {scoring_rate:.0f}% teams scored this game week")