from enum import Enum

class Days(Enum):
    MONDAY = 1
    TUESDAY =2
    WEDNESDAY =3
    THURSDAY= 4
    FRIDAY =5 
    SATURDAY = 6
    SUNDAY =7

def is_weekday(day):
    for x in range(1,8):
        if day.upper() == Days(x).name:
            if x > 5 :
                return False
            return True

print(is_weekday("saturday"))