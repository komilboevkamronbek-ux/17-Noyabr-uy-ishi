class MyDate:    
    def __init__(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana kiritildi")
        self.__day = day
        self.__month = month
        self.__year = year

    MONTHS = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
    "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]
    DAY_IN_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
        
    def isLeapYear(self,year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 ==0
    
    def daysInMonth(self, month, year):
        if month == 2 and self.isLeapYear(year):
            return 29
        return self.DAY_IN_MONTHS[month-1]
    
    def isValidDate(self, day, month, year):
        if year < 1 or year > 9999:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > self.daysInMonth(month, year):
            return False
        return True
        
    
    def setDate(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Noto'g'ri sana kiritildi")
        self.__day = day
        self.__month = month
        self.__year = year
        
    def nextDay(self):
        day = self.__day + 1
        month = self.__month
        year = self.__year
        
        if day > self.daysInMonth(month, year):
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        
        self.setDate(day, month, year)
        return self
    
    def previousDay(self):
        day = self.__day - 1
        month = self.__month
        year = self.__year

        if day < 1:
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            day = self.daysInMonth(month, year)

        self.setDate(day, month, year)
        return self
    
    def nextMonth(self):
        month = self.__month + 1
        year = self.__year
        if month > 12:
            month = 1
            year += 1
        day = min(self.__day, self.daysInMonth(month, year))
        self.setDate(day, month, year)
        return self
    
    def previousMonth(self):
        month = self.__month - 1
        year = self.__year
        if month < 1:
            month = 12
            year -= 1
        day = min(self.__day, self.daysInMonth(month, year))
        self.setDate(day, month, year)
        return self

    def nextYear(self):
        year = self.__year + 1
        day = min(self.__day, self.daysInMonth(self.__month, year))
        self.setDate(day, self.__month, year)
        return self

    def previousYear(self):
        year = self.__year - 1
        day = min(self.__day, self.daysInMonth(self.__month, year))
        self.setDate(day, self.__month, year)
        return self

    def __str__(self):
        return f"{self.__day:02d}-{self.MONTHS[self.__month - 1]} {self.__year} yil"

# Test Case 1: Oddiy sana o'tkazish (Kelasi kun)
# sana = MyDate(15,6,2023)
# sana.nextDay()
# print(sana) #16-Iyun 2023 yil

# Test Case 2: Oy oxiri (Kelasi kun)
# sana = MyDate(30, 4, 2023)
# sana.nextDay()
# print(sana)  # 01-May 2023 yil

# Test Case 3: Yil oxiri (Kelasi kun)
# sana = MyDate(31, 12, 2023)
# sana.nextDay()
# print(sana)  # 01-Yanvar 2024 yil

#Test Case 4: Oy boshlari (O'tgan kun)
# sana = MyDate(1, 5, 2023)
# sana.previousDay()
# print(sana)  # 30-Aprel 2023 yil

#Test Case 5: Kabisa yili (Fevral uchun max kun)
# sana = MyDate(28, 2, 2024)
# sana.nextDay()
# print(sana)  # 29-Fevral 2024 yil

#Test Case 6: Kabisa yili (Fevral 29 dan keyin)
# sana = MyDate(29, 2, 2024)
# sana.nextDay()
# print(sana)  # 01-Mart 2024 yil

#Test Case 7: Kabisa bo'lmagan yilda fevral uchun max kun
# sana = MyDate(28, 2, 2023)
# sana.nextDay()
# print(sana)  # 01-Mart 2023 yil

#Test Case 8: Yil boshiga qaytish (O'tgan kun)
sana = MyDate(1, 1, 2023)
sana.previousDay()
print(sana)  # 31-Dekabr 2022 yil