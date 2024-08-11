class Leave:
    def __init__(self, date, booked, taken, metadata, halfday):
        self.date = date
        self.booked = bool(booked)
        self.taken = bool(taken)
        self.metadata = str(metadata)
        self.halfday = bool(halfday)
    def __str__(self) -> str:
        return f"{self.date} {self.booked} {self.taken} {self.metadata} {self.halfday}"

leaveItems = []

file = open('2024_dates.csv', 'rt') # r = read mode, t = text mode (as opposed to binary)
header = file.readline()
for line in file:
    columns = line.split(',')
    leaveItems.append(Leave(columns[0], columns[1], columns[2], columns[3], columns[4]))
file.close
