

def absolute_diff(dt1, dt2):
    if dt2 < dt1:
        dt1, dt2 = dt2, dt1
    delta = dt2 - dt1
    return delta.days * 86400 + delta.seconds
