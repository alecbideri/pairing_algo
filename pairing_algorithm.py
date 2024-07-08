import random


def pair_teams_for_rounds(teams):
    rounds = []
    team_sides = {team: {'A': 0, 'N': 0} for team in teams}
    opponents = {team: set() for team in teams}

    for round_num in range(3):
        round_pairs = []
        available_teams = list(teams)
        random.shuffle(available_teams)

        while available_teams:
            team1 = available_teams.pop(0)
            possible_opponents = [t for t in available_teams if t not in opponents[team1]]
            
            if not possible_opponents:
                # If no valid opponents, reset and try again
                return pair_teams_for_rounds(teams)
            
            team2 = random.choice(possible_opponents)
            available_teams.remove(team2)

            # Decide sides based on previous rounds
            if team_sides[team1]['A'] < team_sides[team1]['N'] and team_sides[team2]['N'] <= team_sides[team2]['A']:
                affirmative, negative = team1, team2
            elif team_sides[team2]['A'] < team_sides[team2]['N'] and team_sides[team1]['N'] <= team_sides[team1]['A']:
                affirmative, negative = team2, team1
            else:
                affirmative, negative = random.choice([(team1, team2), (team2, team1)])

            round_pairs.append((affirmative, negative))
            team_sides[affirmative]['A'] += 1
            team_sides[negative]['N'] += 1
            opponents[affirmative].add(negative)
            opponents[negative].add(affirmative)

        rounds.append(round_pairs)

    return rounds