n = 4
segments = [
    ("on", 1, 1),
    ("none", 10, 14),
    ("none", 11, 15),
    ("off", 2, 3)
]

min_start, max_start = 0, 1000000
for kind, low, high in reversed(segments):
    if kind == "none":
        min_start = max(min_start, low)
        max_start = min(max_start, high)
    elif kind == "off":
        min_start += low
        max_start += high
    elif kind == "on":
        min_start = max(0, min_start - high)
        max_start = max(0, max_start - low)

min_end, max_end = 0, 1000000
for kind, low, high in segments:
    if kind == "none":
        min_end = max(min_end, low)
        max_end = min(max_end, high)
    elif kind == "on":
        min_end += low
        max_end += high
    elif kind == "off":
        min_end = max(0, min_end - high)
        max_end = max(0, max_end - low)

print(min_start, max_start)
print(min_end, max_end)
