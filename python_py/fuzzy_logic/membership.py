# Fungsi keanggotaan segitiga dan trapesium
def trimf(x, a, b, c):
    if x == b:
        return 1.0
    elif x < a or x > c:
        return 0.0
    elif x < b:
        return (x - a) / (b - a) if b != a else 0
    else:
        return (c - x) / (c - b) if c != b else 0

def trapmf(x, a, b, c, d):
    if x < a or x > d:
        return 0.0
    elif b <= x <= c:
        return 1.0
    elif a <= x < b:
        return (x - a) / (b - a) if b != a else 0
    else:  # c < x <= d
        return (d - x) / (d - c) if d != c else 0
