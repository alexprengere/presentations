

def absolute_diff(dt1, dt2):
    """
    As we saw, this implementation is buggy (on purpose!).
    The correct one would be: abs(dt2.timestamp() - dt1.timestamp())
    """
    if dt2 < dt1:
        dt1, dt2 = dt2, dt1
    delta = dt2 - dt1
    return delta.days * 86400 + delta.seconds
