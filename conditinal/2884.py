h, m = map(int, input().split())
hh = 0
mm = 0
if m - 45 < 0:
    mm = 60 - 45 + m
    if h - 1 < 0:
        hh = 24 - 1
    else:
        hh = h - 1
else:
    hh = h
    mm = m - 45

print(hh, mm)

