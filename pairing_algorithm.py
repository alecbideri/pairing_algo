import random

def pair_teams_for_rounds(teams):
    """
    Generate pairings for debate rounds.

    Args:
    teams (list): A list of team names.

    Returns:
    list: A list of rounds, where each round is a list of tuples (affirmative, negative).
    """
    rounds = []
    # Track the number of times each team has been on each side
    team_sides = {team: {'A': 0, 'N': 0} for team in teams}
    # Track opponents each team has faced
    opponents = {team: set() for team in teams}

    for round_num in range(3):  # Generate 3 rounds of debates
        round_pairs = []
        available_teams = list(teams)
        random.shuffle(available_teams)  # Randomize team order for fairness

        while available_teams:
            team1 = available_teams.pop(0)
            # Find possible opponents (teams not yet faced)
            possible_opponents = [t for t in available_teams if t not in opponents[team1]]
            
            if not possible_opponents:
                # If no valid opponents, restart the entire pairing process
                return pair_teams_for_rounds(teams)
            
            team2 = random.choice(possible_opponents)
            available_teams.remove(team2)

            # Decide sides based on previous rounds to balance affirmative and negative positions
            if team_sides[team1]['A'] < team_sides[team1]['N'] and team_sides[team2]['N'] <= team_sides[team2]['A']:
                affirmative, negative = team1, team2
            elif team_sides[team2]['A'] < team_sides[team2]['N'] and team_sides[team1]['N'] <= team_sides[team1]['A']:
                affirmative, negative = team2, team1
            else:
                # If sides are balanced, randomly assign
                affirmative, negative = random.choice([(team1, team2), (team2, team1)])

            round_pairs.append((affirmative, negative))
            # Update side counts
            team_sides[affirmative]['A'] += 1
            team_sides[negative]['N'] += 1
            # Record that these teams have faced each other
            opponents[affirmative].add(negative)
            opponents[negative].add(affirmative)

        rounds.append(round_pairs)

    return rounds