# Terminal Based Program that can deteremine the day of the week for any given date using an algorithm.


def leap_year(year, month):
    """Returns the month with 100 added to it if its a leap year"""
    if year % 400 != 0 and (year % 100 == 0 or year % 4 != 0
                            or month not in {1, 2}):
        return month
    return month + 100


def doomsday_century(year):
    if (year // 100) in range(3, 1470, 4):
        return 3
    elif (year // 100) in range(0, 1440, 4):
        return 2
    elif (year // 100) in range(1, 1450, 4):
        return 0
    else:
        return 5


def algorithm(year):
    doomsday_2, doomsday_3 = divmod(int(str(year)[2:]), 12)
    doomsday_4 = doomsday_3 // 4
    return doomsday_2 + doomsday_3 + doomsday_4


doomsday_dict1 = {
    'Month': 'Doomsday',
    1: 3,
    101: 4,
    2: 28,
    102: 29,
    3: 14,
    4: 4,
    5: 9,
    6: 6,
    7: 11,
    8: 8,
    9: 5,
    10: 10,
    11: 7,
    12: 12,
}

doomsday_dict2 = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
}

months_dict = {
    1: 31,
    101: 31,
    2: 28,
    102: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def main():
    i = 0
    while i == 0:
        date = input('Please input the date in the form (Year/Month/Day):\n')
        if len(date) == 10:
            date = date.split('/')
            year, month, day = int(date[0]), int(date[1]), int(date[2])
            if len(str(year)) == 4 and month <= 12 and day <= months_dict[
                    leap_year(year, month)]:
                i = 1
            else:
                print('Please input a valid date')
        else:
            print('Please input a valid date')

    doomsday = doomsday_dict1[leap_year(year, month)]
    remainder = (doomsday_century(year) + algorithm(year) +
                 abs(day - doomsday)) % 7
    print(f'The date you have inputted is a {doomsday_dict2[remainder]}.')


if __name__ == "__main__":
    main()