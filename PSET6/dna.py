import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print("Usage: python dna.py *.csv *.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    db = []
    with open(sys.argv[1], "r") as file:
        read = csv.DictReader(file)
        for row in read:
            db.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        dna_seq = file.read()
    subseq = list(db[0].keys())[1:]

    # TODO: Find longest match of each STR in DNA sequence
    res = {}
    for sub in subseq:
        res[sub] = longest_match(dna_seq, sub)

    # TODO: Check database for matching profiles
    for person in db:
        match = 0
        for sub in subseq:
            if int(person[sub]) == res[sub]:
                match += 1
        if match == len(subseq):
            print(person["name"])
            return
    print("No match")
    return

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

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
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
