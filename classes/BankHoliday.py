 #!/usr/bin/env python3
from datetime import datetime

class BankHoliday:
    I_O_FORMAT = "%Y-%m-%d"
    def __init__(self, name, date, leaveGained):
        self.name = name
        self.date = date
        self.leaveGained = float(leaveGained)
    def __str__(self) -> str:
        return f"{datetime.strftime(self.date, BankHoliday.I_O_FORMAT)} ({self.formatLeaveGained()}): {self.name}"
    def valueLeaveGained(self) -> float: 
        return float(self.leaveGained if self.isInPast() else 0.0)
    def formatLeaveGained(self) -> str: 
        return "{} {}".format('+' if self.isInPast() else '', self.valueLeaveGained() if self.isInPast() else '----')
    def isInFuture(self) -> bool:
        return self.date > datetime.now()
    def isInPast(self) -> bool:
        return self.date <= datetime.now()
    