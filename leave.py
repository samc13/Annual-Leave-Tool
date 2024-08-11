#!/usr/bin/env python3

class Leave:
    def __init__(self, date, booked, taken, bankholiday, halfday):
        self.date = date
        self.booked = bool(booked.lower() == 'true')
        self.taken = bool(taken.lower() == 'true')
        self.bankholiday = bool(bankholiday)
        self.halfday = bool(halfday.lower() == 'true')
    def __str__(self) -> str:
        return f"{self.date} {self.booked} {self.taken} {self.bankholiday} {self.halfday}"
    
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
    obj = Leave(columns[0], columns[1], columns[2], False, columns[4])
    print("[DEBUG]: {}".format(obj))
    leaveItems.append(obj)
file.close

def convertToLeaveValue(leaveItem): 
    return 0.5 if leaveItem.halfday else 1

takenLeave =  [convertToLeaveValue(l) for l in leaveItems if l.taken == True]
bookedLeave = [convertToLeaveValue(l) for l in leaveItems if l.taken == False and l.booked == True]

print("Total taken leave:  {}".format(sum(takenLeave)))
print("Total booked leave: {}".format(sum(bookedLeave)))