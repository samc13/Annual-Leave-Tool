#!/usr/bin/env python3
from datetime import datetime

class Leave:
    I_O_FORMAT = "%Y-%m-%d"
    def __init__(self, date, booked, taken, bankholiday, halfday, metadata):
        self.date = datetime.strptime(date, Leave.I_O_FORMAT)
        self.booked = bool(booked.lower() == 'true')
        self.taken = bool(taken.lower() == 'true')
        self.bankholiday = bool(bankholiday.lower() == 'true')
        self.halfday = bool(halfday.lower() == 'true')
        self.metadata = metadata
    def __str__(self) -> str:
        return f"{datetime.strftime(self.date, Leave.I_O_FORMAT)} {self.booked} {self.taken} {self.bankholiday} {self.halfday} {self.metadata}"
    def isInFuture(self) -> bool:
        return self.date > datetime.now()
    
class LeaveAllowance: 
    def __init__(self, category, amount):
        self.category = str(category)
        self.amount = int(amount)
    def __str__(self) -> str:
        return f"{self.category}: {self.amount}"
    
class BankHoliday:
    I_O_FORMAT = "%Y-%m-%d"
    def __init__(self, name, date, leaveGained, classification):
        self.name = name
        self.date = date
        self.leaveGained = float(leaveGained)
        self.classification = str(classification)
    def __str__(self) -> str:
        return f"{datetime.strftime(self.date, BankHoliday.I_O_FORMAT)} ({self.valueLeaveGained()}): {self.name} {self.classification}"
    def valueLeaveGained(self) -> float: 
        return float(self.leaveGained if self.date < datetime.now() else 0.0)
    def isInFuture(self) -> bool:
        return self.date > datetime.now()
    def isInPast(self) -> bool:
        return self.date <= datetime.now()
    
class YearAllowance:
    def __init__(self, base, birthday, bonus, bought, bankHoliday) -> None:
        self.base = int(base)
        self.birthday = int(birthday)
        self.bonus = int(bonus)
        self.bought = int(bought)
        self.bankHoliday = float(bankHoliday)
    def total(self) -> int:
        return self.base + self.birthday + self.bonus + self.bought + self.bankHoliday
    def total_str(self):
        return f"{self.total()}"
    def __str__(self) -> str:
        return f"""
    Base          = {self.base}
    Birthday      = {self.birthday}
    Service Bonus = {self.bonus}
    BHs (worked)  = {self.bankHoliday}
    Purchased     = {self.bought}
    TOTAL         = {self.total_str()}"""

allowanceItems = []

allowanceFile = open('2024_allowance.csv', 'rt') # r = read mode, t = text mode (as opposed to binary)
allowanceHeader = allowanceFile.readline()
for line in allowanceFile:
    columns = line.split(',')
    obj = LeaveAllowance(columns[0], columns[1])
    #print("[DEBUG]: {}".format(obj))
    allowanceItems.append(obj)
allowanceFile.close

leaveItems = []

file = open('2024_dates.csv', 'rt') # r = read mode, t = text mode (as opposed to binary)
header = file.readline()
for line in file:
    columns = line.split(',')
    obj = Leave(columns[0], columns[1], columns[2], columns[3], columns[4], columns[5])
    #print("[DEBUG]: {}".format(obj))
    leaveItems.append(obj)
file.close

def calculateValueOfDay(leaveItem): 
    if leaveItem.halfday:   
        return 0.5
    return 1


allBankHolidays = [BankHoliday(l.metadata, l.date, calculateValueOfDay(l), 'leave' if l.taken else 'gain') for l in leaveItems if l.bankholiday]
totalBankHolidays = allBankHolidays.__len__()

leaveGainedFromWorkedBankHolidays = sum(bh.valueLeaveGained() for bh in allBankHolidays)

yearAllowance = YearAllowance(allowanceItems[0].amount, allowanceItems[1].amount, allowanceItems[2].amount, allowanceItems[3].amount, leaveGainedFromWorkedBankHolidays)

print("------------------------------------")
print("BH breakdown: \n{}".format('\n'.join("{} - {}".format(idx + 1, str(x)) for idx, x in enumerate(allBankHolidays))))
print("------------------------------------")
print("2024 Leave breakdown: {}".format(yearAllowance))
print("------------------------------------")

regularLeaveTaken = sum([calculateValueOfDay(l) for l in leaveItems if l.taken or (l.halfday and l.bankholiday)])
regularLeaveBooked = sum([calculateValueOfDay(l) for l in leaveItems if not(l.taken) and l.booked])
upcomingBankHolidays = sum([1 for bh in allBankHolidays if bh.isInFuture()])
upcomingBankHolidaysBookedOff = sum([calculateValueOfDay(l) for l in leaveItems if l.isInFuture() and l.booked and l.bankholiday])
leaveRemaining = yearAllowance.total() - regularLeaveTaken

print("Used so far                          : {}".format(regularLeaveTaken))
print("BHs remaining this year              : {}".format(upcomingBankHolidays))
print("     of which already booked off     : {}".format(upcomingBankHolidaysBookedOff))
print("------------------------------------")
print("Final total (remaining, booked)      : {} ({}, {})".format(leaveRemaining - regularLeaveBooked, leaveRemaining, regularLeaveBooked))
print("     with N more if BH worked        : {}".format(upcomingBankHolidays - upcomingBankHolidaysBookedOff))