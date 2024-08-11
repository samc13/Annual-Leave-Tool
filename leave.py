import numpy as np

class Leave:
    def __init__(self, date, booked, taken, metadata, halfday):
        self.date = date
        self.booked = bool(booked)
        self.taken = bool(taken)
        self.metadata = str(metadata)
        self.halfday = bool(halfday)
    def __str__(self) -> str:
        return f"{self.date} {self.booked} {self.taken} {self.metadata} {self.halfday}"
    
class Allowance:
    def __init__(self, base, birthday, bonus, bought, bankHoliday) -> None:
        self.base = int(base)
        self.birthday = int(birthday)
        self.bonus = int(bonus)
        self.bought = int(bought)
        self.bankHoliday = int(bankHoliday)
    def total(self):
        self.base + self.birthday + self.bonus + self.bought + self.bankHoliday

leaveItems = []

file = open('2024_dates.csv', 'rt') # r = read mode, t = text mode (as opposed to binary)
header = file.readline()
for line in file:
    columns = line.split(',')
    leaveItems.append(Leave(columns[0], columns[1], columns[2], columns[3], columns[4]))
file.close

takenLeave = [l for l in leaveItems if l.taken == True]
bookedLeave = [l for l in leaveItems if l.taken == False and l.booked == True]


print("Total taken leave:  {}".format(len(takenLeave)))
print("Total booked leave: {}".format(len(bookedLeave)))