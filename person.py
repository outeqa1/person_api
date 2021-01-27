import calculations


class Person:
    def __init__(self, iin: str):
        self.iin = iin
        self.age = calculations.calculate_age(iin)

    def get_json(self):
        return {
            "iin": self.iin,
            "age": self.age
        }


def iin_is_valid(iin: str) -> bool:
    day = iin[4:6]
    month = iin[2:4]

    if len(iin) != 12 or not iin.isdigit():
        return False
    if int(day) > 31 or int(month) > 12:
        return False

    return True
