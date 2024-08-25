#!/usr/bin/env python3

class LeaveAllowance: 
    def __init__(self, category, amount):
        self.category = str(category)
        self.amount = int(amount)
    def __str__(self) -> str:
        return f"{self.category}: {self.amount}"
    