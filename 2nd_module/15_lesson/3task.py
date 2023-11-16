class Date:
    def __init__(self, day: int, month: int, year: int):
        self.set_day(day)
        self.set_month(month)
        self.set_year(year)

    @property
    def day(self) -> int:
        return self._day

    @property
    def month(self) -> int:
        return self._month

    @property
    def year(self) -> int:
        return self._year

    def set_day(self, day: int) -> None:
        if 1 <= day <= 31:
            self._day = day
        else:
            raise ValueError("Invalid day value")

    def set_month(self, month: int) -> None:
        if 1 <= month <= 12:
            self._month = month
        else:
            raise ValueError("Invalid month value")

    def set_year(self, year: int) -> None:
        if year >= 0:
            self._year = year
        else:
            raise ValueError("Invalid year value")

    def __str__(self) -> str:
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    @staticmethod
    def is_date_valid(date_str: str) -> bool:
        try:
            Date.from_string(date_str)
            return True
        except ValueError:
            return False

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
