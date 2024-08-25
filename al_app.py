#!/usr/bin/env python3
from classes.LeaveAllowance import LeaveAllowance
from classes.Leave import Leave
from classes.BankHoliday import BankHoliday
from classes.YearAllowance import YearAllowance
import config.config as configuration
   
allowanceItems = []

allowanceFile = open(configuration.ANNUAL_LEAVE_ALLOWANCE_FILEPATH, 'rt') # r = read mode, t = text mode (as opposed to binary)
allowanceHeader = allowanceFile.readline()
for line in allowanceFile:
    columns = line.split(',')
    obj = LeaveAllowance(columns[0], columns[1])
    #print("[DEBUG]: {}".format(obj))
    allowanceItems.append(obj)
allowanceFile.close

leaveItems = []

file = open(configuration.ANNUAL_LEAVE_USAGE_FILEPATH, 'rt') # r = read mode, t = text mode (as opposed to binary)
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


allBankHolidays = [BankHoliday(l.metadata, l.date, calculateValueOfDay(l)) for l in leaveItems if l.bankholiday]
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

print("Total leave accumulated for year     : {}".format(yearAllowance.total()))
print("     (Note that this excludes A/L that can still be gained by working upcoming BHs)")
print("Used so far                          : {}".format(regularLeaveTaken))
print("Upcoming booked annual leave         : {}".format(regularLeaveBooked))
print("BHs remaining this year              : {}".format(upcomingBankHolidays))
print("     of which already booked off     : {}".format(upcomingBankHolidaysBookedOff))
print("------------------------------------")
print("Final total (remaining, booked)      : {} ({}, {})".format(leaveRemaining - regularLeaveBooked, leaveRemaining, regularLeaveBooked))
print("     with N more if BH worked        : {}".format(upcomingBankHolidays - upcomingBankHolidaysBookedOff))