def unique_in_order(iterable):
    result = []
    prev = None
    for item in iterable:
        if item != prev:
            result.append(item)
            prev = item
    return result
