from datetime import date


def calculate_age(iin: str) -> int:
    day = iin[4:6]
    month = iin[2:4]
    year = convert_year(iin[:2])

    born = date(int(year), int(month), int(day))
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


def convert_year(short_year: str):
    if int(short_year) > 21:
        return "19" + short_year
    return "20" + short_year
