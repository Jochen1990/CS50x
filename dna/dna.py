import csv
import sys
from sys import argv


def main():

    # TODO: Check for command-line usage
    if (len(argv) != 3):
        print("Incorrect usage")

    # TODO: Read database file into a variable
    database = []
    with open(argv[1]) as file:
        file_reader = csv.DictReader(file)
        for row in file_reader:
            database.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2]) as file:
        seq = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    strings = list(database[1].keys())[1:]
    results = {}
    for subsequence in strings:
        results[subsequence] = longest_match(seq, subsequence)
    print(strings)
    print(results)

    # TODO: Check database for matching profiles

    for person in database:
        match = True
        for subsequence in strings:
            if int(person[subsequence]) != results[subsequence]:
                match = False
                break
        if match:
            print(person["name"])
            return
    print("No match")
    return


def longest_match(seq, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(seq)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if seq[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
