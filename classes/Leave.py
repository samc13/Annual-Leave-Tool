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