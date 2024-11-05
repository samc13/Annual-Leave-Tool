#!/usr/bin/env python3
from datetime import datetime

class Leave:
    I_O_FORMAT = "%Y-%m-%d"
    def __init__(self, date, bankholiday, balancechange, metadata):
        self.date = datetime.strptime(date, Leave.I_O_FORMAT)
        self.bankholiday = bool(bankholiday.lower() == 'bh')
        self.balancechange = float(balancechange or 0)
        self.metadata = metadata
    def __str__(self) -> str:
        return f"{datetime.strftime(self.date, Leave.I_O_FORMAT)} {self.bankholiday} {self.balancechange} {self.metadata}"
    def isInFuture(self) -> bool:
        return self.date > datetime.now()
    def isBankHoliday(self) -> bool: 
        return self.bankholiday