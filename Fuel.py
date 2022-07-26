from datetime import timedelta
from datetime import datetime

refillDate = input('When did you last refill? yy-mm-dd')
aveMilesPerWeek = 158.4 #float(input('How many miles you did you do last week? '))
mpg = 37.9 #float(input('What is your current mpg? '))
tankCapacity = 30 #int(input('How many litres before you want to refill your car? '))

fuelUsedPerDay = round(((aveMilesPerWeek/mpg)*4.546)/7)
dateRefill = tankCapacity/fuelUsedPerDay
nextRefill = (datetime.strptime(refillDate, "%Y-%m-%d")) + timedelta(days=dateRefill)

print(nextRefill)
