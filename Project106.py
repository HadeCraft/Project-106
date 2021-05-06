import numpy
import csv

def getDataSource(data_path):
    CoffeeInSI = []
    HoursOfSleep = []

    with open(data_path) as c:
        reader = csv.DictReader(c)

        for row in reader:
            CoffeeInSI.append(float(row["Coffee in ml"]))
            HoursOfSleep.append(float(row["sleep in hours"]))

            