"""
    This program prompts for a txt.file, then opens the text file,
    reads the data, filters out all the data containing the e-mails
    received in the year 2008 and counts for every hour how many
    e-mails were received.

    Input:
        from "mbox-short.txt":
            "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
        Return-Path: <postmaster@collab.sakaiproject.org>
        Received: from murder (mail.umich.edu [141.211.14.90])
             by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
             Sat, 05 Jan 2008 09:14:16 -0500
             [...] "
    Output:
            04 3
            06 1
            07 1
            09 2
            10 3
            11 6
            14 1
            15 2
            16 4
            17 2
            18 1
            19 1

"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.strip()
    if not line.startswith('From'):
        continue
    if not line.endswith('2008'):
        continue

    list_0 = line.split()  # here we break the line in words
    # here we select the time from the sequence where time is the 5th element
    # and we break the time string using the : symbol into more pieces
    time = list_0[5].split(":")
    hour = time[0]  # here we assign to hour variable the first piece from the sequence above which is the hour

    # here we create a dictionary where we create
    # a list of hours in the dictionary using
    # keys as hours and incrementing values
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] += 1
    # here we create a new list where we bring all
    # the elements (key-value) from the dictionary
    list_1 = list(counts.items())
    # here we sort the list after the keys
    list_1.sort()

for key, value in list_1:
    # in the end we choose to print the key, values from the sorted list
    print(key, value)
