#Christopher Louie
#Death Row Coders
#SoftDev
#File Reading
#2024/9/18
#Time Spent: 30

import random
import csv

occupationsList = []

with open("occupations.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        job = row[0]
        percentage = float(row[1])
        if job != "Total":
            occupationsList.append((job, percentage))

def randomOccupation():
    percentagesum = sum(job[1] for job in occupationsList)
    if percentagesum == 0:
        return None
    x = random.uniform(0, percentagesum)
    for job, percentage in occupationsList:
        x -= percentage
        if x <= 0:
            return job
    return None

print(randomOccupation())
