import os
import pandas as pd
from IPython.display import FileLink

# Load the dataset
df = pd.read_csv('Resources/election_data.csv')

# Calculate the total number of votes cast
total_votes = df.shape[0]

# Get a complete list of candidates who received votes
candidates = df['Candidate'].unique()

# Calculate the total number of votes each candidate won
vote_counts = df['Candidate'].value_counts()

# Calculate the percentage of votes each candidate won
vote_percentages = (vote_counts / total_votes) * 100

# Determine the winner of the election based on popular vote
winner = vote_counts.idxmax()

# Prepare the output
output = (
    "Election Results\n"
    "----------------------------\n"
    f"Total Votes: {total_votes}\n"
    "----------------------------\n"
)

for candidate in candidates:
    output += f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})\n"

output += "----------------------------\n"
output += f"Winner: {winner}\n"
output += "----------------------------"

# Print the output
print(output)

# Export the results to a text file in the specified directory
output_directory = 'analysis'
output_path = f'{output_directory}/election_results.txt'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

with open(output_path, 'w') as file:
    file.write(output)

# Display a link to download the file
display(FileLink(output_path))
