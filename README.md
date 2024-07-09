# Debate Team Pairing System

## Overview

This Debate Team Pairing System is an automated tool designed to generate fair and balanced pairings for multiple rounds of debate competitions. It provides an efficient way to organize debate tournaments by reading team names from a file, creating pairings for a user-specified number of rounds, and outputting the results to a file.

## Features

- Read team names from a text file
- Generate pairings for a custom number of debate rounds
- Ensure teams don't face the same opponent twice (when possible)
- Balance affirmative and negative positions for each team
- Output pairings to a text file

## Installation

1. Clone this repository:
2. Navigate to the project directory:
3. ## Requirements

- Python 3.x

No additional libraries are required.

## Usage

1. Prepare a text file with the list of team names, one per line.
2. Run the main script:
3. Follow the prompts to:
- Enter the name of your input file
- Specify the number of debate rounds
- Provide a name for the output file
4. The system will generate the pairings and save them to the output file.

## Project Structure

- `main.py`: The main script to run the application
- `file_operations.py`: Handles file reading and writing operations
- `pairing_algorithm.py`: Contains the core algorithm for pairing teams

## Documentation

For detailed information about the system, including in-depth explanations of each module, the pairing algorithm, and system workflow, please refer to our [[comprehensive documentation]](https://docs.google.com/document/d/13PBxqHZKgVKr74JSMrDUKBkW_7QelhQ1R-2wExXM4x4/edit).

## Contributing

Contributions to improve the Debate Team Pairing System are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
