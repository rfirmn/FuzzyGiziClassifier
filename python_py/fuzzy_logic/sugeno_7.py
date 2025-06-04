from .membership import trimf, trapmf

def fuzzy_sugeno_7(berat, tinggi):
    tinggi_pendek = trimf(tinggi, 50, 50, 82)
    tinggi_sedang = trimf(tinggi, 65, 90, 125)
    tinggi_tinggi = trapmf(tinggi, 110, 125, 200, 200)

    berat_pendek = trimf(berat, 10, 10, 20)
    berat_sedang = trimf(berat, 15, 19, 24)
    berat_tinggi = trapmf(berat, 22, 28, 36, 36)

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
