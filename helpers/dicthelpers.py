def increase_or_update(d: dict, key, number):
    d[key] = d[key] + number if key in d else number
