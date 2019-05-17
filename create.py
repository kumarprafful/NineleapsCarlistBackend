from cars.models import CarSet
import csv

path ='CarsDataset-Sheet1.csv'

with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        created = CarSet.objects.create(
            car_name=row[0],
            mpg=row[1],
            cylinders=row[2],
            displacement=row[3],
            horsepower=row[4],
            weight=row[5],
            acceleration=row[6],
            model=row[7],
            origin=row[8],

            )
