def calculate_score(participant):
    # calculate total score based on point system
    return participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2

def create_scoreboard(participants):
    # Loop through each partcipant
    scoreboard = []
    for participant in participants:
        score = calculate_score(participant)
        # Add participant with score to scoreboard
        scoreboard.append({'name': participant['name'], 'score': score})
    
    # Sort the scoreboard by score(descending) and then by name(ascending)
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard

participants = [
  {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
  {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = create_scoreboard(participants)
print(scoreboard)
