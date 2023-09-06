age: int
age = 's'
# name: str
# salary: float
# is_month_end: bool

def Sum(x: int, y: int):
    return x + y


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return 'can_drive'


print(police_check(20))
