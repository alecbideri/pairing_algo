from file_operations import read_teams_from_file, write_results_to_file
from pairing_algorithm import pair_teams_for_rounds

def main():
    while True:
        filename = input("Enter the filename or path of the file containing team names (e.g., teams.txt): ")
        if filename.lower().endswith('.py'):
            print("Error: This appears to be a Python file. Please enter the name of the text file containing team names.")
            continue
        try:
            teams = read_teams_from_file(filename)
            break
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please make sure you've entered the correct filename or path.")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except OSError:
            print("Error: Invalid filename or path. Please try again.")
        
        retry = input("Would you like to try entering the filename again? (yes/no): ")
        if retry.lower() != 'yes':
            return

    rounds = pair_teams_for_rounds(teams)
    
    output_filename = input("Enter the filename for the output results (e.g., debate_pairings.txt): ")
    write_results_to_file(rounds, output_filename)
    print(f"Results have been written to {output_filename}")

if __name__ == "__main__":
    main()