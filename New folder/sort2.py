import csv
from itertools import islice

with open('ua.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in islice(reader, 10): 
        print(row['tweet'])
