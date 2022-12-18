def increase_or_update(d: dict, key, number):
    d[key] = d[key] + number if key in d else number


def create_or_append(d: dict, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]
