def length(id):
    if len(id) == 13:
        return True
    else:
        return False


def digits_only(id):
    if id.isdigit():
        return True
    else:
        return False


def days(id):
    day = int(id[4:6])
    year = int(id[0:2])
    month = int(id[2:4])
    if year % 4 == 0 and month == 2 and 0 < day <= 29:
        return True
    if year % 4 != 0 and month == 2 and 0 < day <= 28:
        return True
    if month in [1, 3, 5, 7, 8, 10, 12] and 0 < day <= 31:
        return True
    if month in [4, 6, 9, 11] and 0 < day <= 30:
        return True
    else:
        return False


def month(id):
    month = int(id[2:4])
    if 1 <= month <= 12:
        return True
    else:
        return False


def gender(id):
    gender = int(id[6:10])
    if 0000 <= gender <= 9999:
        return True
    else:
        return False


def citizenship(id):
    citizenship = int(id[9])
    if citizenship == 1 or citizenship == 0:
        return True
    else:
        return False


def check_sum(id):
    digits = list(map(int, str(id)))
    oddSum = sum(digits[-1::-2])
    evnSum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    if (oddSum + evnSum) % 10 == 0:
        return True
    else:
        return False


def validate_sa_id(id):
    if (
        not length(id)
        or not digits_only(id)
        or not days(id)
        or not month(id)
        or not gender(id)
        or not check_sum(id)
    ):
        return False

    return True


