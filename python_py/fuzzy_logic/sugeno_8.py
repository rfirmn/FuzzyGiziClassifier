from .membership import trimf, trapmf

def fuzzy_sugeno_8(berat, tinggi):
    tinggi_pendek = trimf(tinggi, 50, 50, 90)
    tinggi_sedang = trimf(tinggi, 75, 100, 125)
    tinggi_tinggi = trapmf(tinggi, 115, 145, 200, 200)

    berat_pendek = trimf(berat, 10, 10, 22)
    berat_sedang = trimf(berat, 20, 27, 32)
    berat_tinggi = trapmf(berat, 27, 24, 56, 56)

    rules = [
        (min(berat_pendek, tinggi_pendek), 1),
        (min(berat_pendek, tinggi_sedang), 1),
        (min(berat_pendek, tinggi_tinggi), 1),
        (min(berat_sedang, tinggi_pendek), 1),
        (min(berat_sedang, tinggi_sedang), 2),
        (min(berat_sedang, tinggi_tinggi), 2),
        (min(berat_tinggi, tinggi_pendek), 1),
        (min(berat_tinggi, tinggi_sedang), 2),
        (min(berat_tinggi, tinggi_tinggi), 3)
    ]

    numerator = sum(strength * output for strength, output in rules)
    denominator = sum(strength for strength, _ in rules)
    return numerator / denominator if denominator != 0 else 0
