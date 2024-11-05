#!/usr/bin/env python3
from classes.LeaveAllowance import LeaveAllowance
from classes.Leave import Leave
from classes.BankHoliday import BankHoliday
from classes.YearAllowance import YearAllowance
import config.config as configuration
import itertools
   
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

datesFile = open(configuration.ANNUAL_LEAVE_USAGE_FILEPATH, 'rt') # r = read mode, t = text mode (as opposed to binary)
header = datesFile.readline()
for line in datesFile:
    columns = line.split(',')
    obj = Leave(columns[0], columns[1], columns[2], columns[3])
    #print("[DEBUG]: {}".format(obj))
    leaveItems.append(obj)
datesFile.close

allBankHolidays = [BankHoliday(l.metadata, l.date, l.balancechange) for l in leaveItems if l.bankholiday]

leaveGainedFromWorkedBankHolidays = sum(bh.valueLeaveGained() for bh in allBankHolidays)

yearAllowance = YearAllowance(allowanceItems[0].amount, allowanceItems[1].amount, allowanceItems[2].amount, allowanceItems[3].amount, leaveGainedFromWorkedBankHolidays)

regularLeave = [l for l in leaveItems if not(l.isBankHoliday())]
bankHolidayLeave = [l for l in leaveItems if l.isBankHoliday()]
regularLeaveTaken = sum([-l.balancechange for l in regularLeave if not(l.isInFuture())])
totalBankHolidays = sum([1 for l in leaveItems if l.isBankHoliday()])
regularLeaveUpcoming = sum([-l.balancechange for l in regularLeave if l.isInFuture()])
groupedLeaveIterator = itertools.groupby(regularLeave, lambda x : x.metadata) # nb iterator can only be used once

print("------------------------------------")
print("Summary of holiday used:")
for key, group in groupedLeaveIterator:
    print("  - {} {}".format(key, sum([x.balancechange for x in group])))
print("Total used so far: {}".format(regularLeaveTaken))
print("Total booked:      {}".format(regularLeaveUpcoming))

print("------------------------------------")
print("BH breakdown: \n{}".format('\n'.join("{} - {}".format(idx + 1, str(x)) for idx, x in enumerate(allBankHolidays))))
print("    Total:      + {}".format(leaveGainedFromWorkedBankHolidays))
print("------------------------------------")
print("Year Leave breakdown: {}".format(yearAllowance))
print("------------------------------------")

regularLeaveBooked = sum([-l.balancechange for l in leaveItems if l.isInFuture()])
upcomingBankHolidays = sum([1 for bh in allBankHolidays if bh.isInFuture()])
upcomingBankHolidaysBookedOff = float(sum([1 for l in bankHolidayLeave if l.isInFuture() and l.balancechange == 0.0]))

print("Regular leave used so far            : {}".format(regularLeaveTaken))
print("Upcoming booked annual leave         : {} (+ BH {})".format(regularLeaveBooked, upcomingBankHolidaysBookedOff))
print("Total usage (incl. booked)           : {}".format(regularLeaveTaken + regularLeaveBooked))
print("    of total accrued days            : {}".format(yearAllowance.total()))
print("Remaining leave to take              : {}".format(yearAllowance.total() - regularLeaveTaken - regularLeaveBooked))
print("------------------------------------")