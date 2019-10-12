def MediaHarmonicaDeTupla(*numbers):
    denom = 0
    for num in numbers:
        denom = denom + 1/num
    return len(numbers)/denom


media_harm = MediaHarmonicaDeTupla(1, 2, 3, 4, 5)
print(media_harm)
