import os
import csv

poll_data_csv = os.path.join('PollData.csv')

total_votes = 0
candidates_unique= []
candidate_vote_count = []

with open(poll_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_in = (row[2])
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)
pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)

    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x
election_winner = candidates_unique[max_index]  

print(f'Total Votes:{total_votes}')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print(f"Election winner: {election_winner.upper()}")

output_file - os.path.join("pypoll_election_results.txt")
with open(output_file, "w", newline="")as datafile:
    datafile.write(f'Total Votes: {total_votes}/n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {pct[x]}% ( {candidate_vote_count[x]})/n')
    datafile.write(f'Election Winner: {election_winner.upper()/n}')
