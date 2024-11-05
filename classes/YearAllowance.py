 #!/usr/bin/env python3

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
    TOTAL         = {self.total_str()}
        (Note that this excludes A/L that can still be gained by working upcoming BHs)"""
