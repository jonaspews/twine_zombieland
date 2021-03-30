import csv

cities = []

with open('world-cities_only_csv.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        cities.append(row[0])
        
print(cities)
