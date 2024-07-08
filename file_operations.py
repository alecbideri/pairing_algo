import os

def read_teams_from_file(filename):
    try:
        with open(filename, 'r') as file:
            teams = [line.strip() for line in file if line.strip()]
        if len(teams) % 2 != 0:
            raise ValueError("The number of teams must be even.")
        return teams
    except FileNotFoundError:
        # If file not found, try to look in the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, filename)
        try:
            with open(full_path, 'r') as file:
                teams = [line.strip() for line in file if line.strip()]
            if len(teams) % 2 != 0:
                raise ValueError("The number of teams must be even.")
            return teams
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filename}")

def write_results_to_file(rounds, output_filename):
    with open(output_filename, 'w') as file:
        for round_num, round_pairs in enumerate(rounds, 1):
            file.write(f"Round {round_num} Debate Pairings:\n")
            file.write("Affirmative\t\tNegative\n")
            for affirmative, negative in round_pairs:
                file.write(f"{affirmative}\t\t{negative}\n")
            file.write("\n")