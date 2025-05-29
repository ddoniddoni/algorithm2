hh, mm = map(int, input().split())
need = int(input())

mm += need

if mm >= 60:
    hh += mm // 60
    mm = mm % 60

if hh >= 24:
    hh = hh % 24

print(hh,mm)


