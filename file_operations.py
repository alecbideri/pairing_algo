import os

def read_teams_from_file(filename):
    """
    Read team names from a file and return them as a list.
    
    Args:
    filename (str): Name of the file containing team names.
    
    Returns:
    list: A list of team names.
    
    Raises:
    FileNotFoundError: If the file is not found.
    ValueError: If the number of teams is not even.
    """
    def read_and_validate(file_path):
        with open(file_path, 'r') as file:
            # Read non-empty lines and strip whitespace
            teams = [line.strip() for line in file if line.strip()]
        
        # Check if the number of teams is even
        if len(teams) % 2 != 0:
            raise ValueError("The number of teams must be even.")
        return teams

    try:
        # Try to read the file from the given filename
        return read_and_validate(filename)
    except FileNotFoundError:
        # If file not found, try to look in the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, filename)
        try:
            return read_and_validate(full_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filename}")

def write_results_to_file(rounds, output_filename):
    """
    Write debate pairings to an output file.
    
    Args:
    rounds (list): A list of rounds, where each round is a list of team pairings.
    output_filename (str): Name of the file to write the results to.
    """
    with open(output_filename, 'w') as file:
        for round_num, round_pairs in enumerate(rounds, 1):
            # Write round number
            file.write(f"Round {round_num} Debate Pairings:\n")
            # Write column headers
            file.write("Affirmative\t\tNegative\n")
            # Write team pairings
            for affirmative, negative in round_pairs:
                file.write(f"{affirmative}\t\t{negative}\n")
            # Add a blank line between rounds
            file.write("\n")