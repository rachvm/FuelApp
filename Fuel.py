from datetime import timedelta
from datetime import datetime

refillDate = input('When did you last refill? dd-mm-yyyy')
aveMilesPerWeek = float(input('How many miles you did you do last week? '))
mpg = float(input('What is your current mpg? '))
tankCapacity = int(input('How many litres before you want to refill your car? '))

fuelUsedPerDay = round(((aveMilesPerWeek/mpg)*4.546)/7)
dateRefill = tankCapacity/fuelUsedPerDay
nextRefill = (datetime.strptime(refillDate, "%d-%m-%Y")) + timedelta(days=dateRefill)

print(nextRefill)
