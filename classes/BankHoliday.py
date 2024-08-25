 #!/usr/bin/env python3
from datetime import datetime

class BankHoliday:
    I_O_FORMAT = "%Y-%m-%d"
    def __init__(self, name, date, leaveGained):
        self.name = name
        self.date = date
        self.leaveGained = float(leaveGained)
    def __str__(self) -> str:
        return f"{datetime.strftime(self.date, BankHoliday.I_O_FORMAT)} ({self.valueLeaveGained()}): {self.name}"
    def valueLeaveGained(self) -> float: 
        return float(self.leaveGained if self.date < datetime.now() else 0.0)
    def isInFuture(self) -> bool:
        return self.date > datetime.now()
    def isInPast(self) -> bool:
        return self.date <= datetime.now()
    