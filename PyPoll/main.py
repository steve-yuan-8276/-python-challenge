import csv
import os

# Getting the folder's path
election_csv = os.path.join(".", "Resources", "election_data.csv")

# Define the Function
def election_results(election_csv):
    votes = []
    candidates = []

    # Read data into list
    with open(election_csv, newline='') as election_data:
        csvreader = csv.reader(election_data, delimiter=',')
        header = next(csvreader) #skip the header row
        for row in csvreader:
            votes.append(row[0])
            candidates.append(row[2])

    # Calculate the total votes
    total_votes = len(votes)

    # Calculate each candidate's votes
    charles_votes_count = candidates.count("Charles Casper Stockham")
    diana_votes_count = candidates.count("Diana DeGette")
    raymond_votes_count = candidates.count("Raymon Anthony Doane")

    #Calculate the vote percentage of each candidate
    charles_votes_percent = round(((charles_votes_count / total_votes) * 100),3)
    diana_votes_percent = round(((diana_votes_count / total_votes) * 100),3)
    raymond_votes_percent = round(((raymond_votes_count / total_votes) * 100),3)

    # Find the winner of the election based on popular vote
    if (charles_votes_percent> diana_votes_percent) and (charles_votes_percent > raymond_votes_percent):
        winner = "Charles Casper Stockham"
    elif (diana_votes_percent > charles_votes_percent) and (diana_votes_percent > raymond_votes_percent):
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"


    # print the reasults
    print(f"Election Results")
    print(f"-----------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-----------------------")
    print(f"Charles Casper Stockham: {charles_votes_percent}% ({charles_votes_count})")
    print(f"Diana DeGette: {diana_votes_percent}% ({diana_votes_count})")
    print(f"Raymon Anthony Doane: {raymond_votes_percent}% ({raymond_votes_count})")
    print(f"-----------------------")
    print(f"Winner: {winner}")
    print(f"-----------------------")

    # Write the results into election_results.txt
    output_file = os.path.join(".", "analysis", "election_results.txt")
    with open(output_file, "w", newline="") as file:
        file.write("Election Results\n")
        file.write("----------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("----------------------\n")
        file.write(f"Charles Casper Stockham: {charles_votes_percent}% ({charles_votes_count})\n")
        file.write(f"Diana DeGette: {diana_votes_percent}% ({diana_votes_count})\n")
        file.write(f"Raymon Anthony Doane: {raymond_votes_percent}% ({raymond_votes_count})\n")
        file.write(f"-----------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write(f"-----------------------\n")

# Call the function
election_results(election_csv)