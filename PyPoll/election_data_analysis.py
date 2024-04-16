import os
import csv

# Path to the CSV file
file_path = os.path.join("election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')

    # Skip the header row
    next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Count the votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
results = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results[candidate] = (percentage, votes)

    # Determine the winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (percentage, votes) in results.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = "election_results.txt"
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, (percentage, votes) in results.items():
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print("Results have been saved to 'election_results.txt'")