from datetime import timedelta


def add_gigasecond(birth_date):
    birth_date +=timedelta(seconds=10 ** 9)
    print(birth_date)
    return birth_date