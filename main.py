from file_operations import read_teams_from_file, write_results_to_file
from pairing_algorithm import pair_teams_for_rounds

def main():
    """
    Main function to run the debate pairing program.
    """
    while True:
        # Prompt user for input file name
        filename = input("Enter the filename or path of the file containing team names (e.g., teams.txt): ")
        
        # Check if the file is a Python file
        if filename.lower().endswith('.py'):
            print("Error: This appears to be a Python file. Please enter the name of the text file containing team names.")
            continue
        
        try:
            # Attempt to read teams from the file
            teams = read_teams_from_file(filename)
            break  # Exit the loop if successful
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please make sure you've entered the correct filename or path.")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except OSError:
            print("Error: Invalid filename or path. Please try again.")
        
        # Ask if the user wants to retry
        retry = input("Would you like to try entering the filename again? (yes/no): ")
        if retry.lower() != 'yes':
            return  # Exit the function if user doesn't want to retry

    # Generate debate pairings
    rounds = pair_teams_for_rounds(teams)
    
    # Prompt user for output file name
    output_filename = input("Enter the filename for the output results (e.g., debate_pairings.txt): ")
    
    # Write results to the output file
    write_results_to_file(rounds, output_filename)
    print(f"Results have been written to {output_filename}")

if __name__ == "__main__":
    main()