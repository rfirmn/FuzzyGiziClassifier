import numpy as np
from .membership import trimf, trapmf

def fuzzy_mamdani_7(berat, tinggi):
    tinggi_pendek = trimf(tinggi, 50, 50, 82)
    tinggi_sedang = trimf(tinggi, 65, 90, 125)
    tinggi_tinggi = trapmf(tinggi, 110, 125, 200, 200)

    berat_pendek = trimf(berat, 10, 10, 20)
    berat_sedang = trimf(berat, 15, 19, 24)
    berat_tinggi = trapmf(berat, 22, 28, 36, 36)

    rules = [
        (min(berat_pendek, tinggi_pendek), 'kurang'),
        (min(berat_pendek, tinggi_sedang), 'kurang'),
        (min(berat_pendek, tinggi_tinggi), 'kurang'),
        (min(berat_sedang, tinggi_pendek), 'kurang'),
        (min(berat_sedang, tinggi_sedang), 'baik'),
        (min(berat_sedang, tinggi_tinggi), 'baik'),
        (min(berat_tinggi, tinggi_pendek), 'kurang'),
        (min(berat_tinggi, tinggi_sedang), 'baik'),
        (min(berat_tinggi, tinggi_tinggi), 'sangat_baik')
    ]

    universe = np.linspace(0, 3, 100)
    output_kurang = [trimf(u, 0, 0, 1.4) for u in universe]
    output_baik = [trimf(u, 1, 1.8, 2.5) for u in universe]
    output_sangat_baik = [trimf(u, 2, 3, 3) for u in universe]

    aggregated = np.zeros_like(universe)
    for strength, label in rules:
        if strength == 0:
            continue
        if label == 'kurang':
            fuzzy_set = [min(strength, val) for val in output_kurang]
        elif label == 'baik':
            fuzzy_set = [min(strength, val) for val in output_baik]
        elif label == 'sangat_baik':
            fuzzy_set = [min(strength, val) for val in output_sangat_baik]
        aggregated = np.maximum(aggregated, fuzzy_set)

    numerator = np.sum(universe * aggregated)
    denominator = np.sum(aggregated)
    return numerator / denominator if denominator != 0 else 0
