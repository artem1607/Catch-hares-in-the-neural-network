import math
import numpy
import random
f=open('square', 'w')
f.write('''<?xml version="1.0" encoding="utf-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1700px" height="1700px">\n''')
tochki = []
for i in range(5):
    a = random.randint(40, 500)
    b = random.randint(40, 500)
    tochki.append((a, b))
    f.write(f'''<circle cx="{a}" cy="{b}"  r="2" stroke="blue" stroke-width="2"/>\n''')
alfa = 0
v = []
g = []
degrees = []
alfiki = []
for i in range(1, 361):
    alfa = 2 * math.pi / 360 * i
    pmux = -999
    xox = 0
    yoy = 0
    degr = 0
    alfs = 0
    for peg in tochki:
        pmax = peg[0] * math.cos(alfa) + peg[1] * math.sin(alfa)
        if pmax >= pmux:                   
            pmux = pmax
            xox = peg[0]
            yoy = peg[1]
            degr = alfa
            alfs = alfa
    alfiki.append(alfs)
    degrees.append(degr)
    v.append(xox)
    g.append(yoy)
print('Точки\t', '          Расстояние')
dd = []
ymax = max(g)
ymin = min(g)
xmax = max(v)
xmin = min(v)
xcir = (xmax - xmin) / 2
ycir = (ymax - ymin) / 2
print(xmin, xmax, ymin, ymax)
f.write(f'''<line  x1="{xmin}" y1="{ymin}" x2="{xmax}" y2="{ymin}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
f.write(f'''<line  x1="{xmin}" y1="{ymin}" x2="{xmin}" y2="{ymax}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
f.write(f'''<line  x1="{xmax}" y1="{ymin}" x2="{xmax}" y2="{ymax}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
f.write(f'''<line  x1="{xmin}" y1="{ymax}" x2="{xmax}" y2="{ymax}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
summg = 0
skv = (xmax - xmin) * (ymax - ymin)
for i in range(len(v)):
    vov2 = v[i - 1]
    gog2 = g[i - 1]
    vov1 = v[i]
    gog1 = g[i]
    
    f.write(f'''<line  x1="{vov1}" y1="{gog1}" x2="{vov2}" y2="{gog2}" style="stroke:rgb(168,228,160);stroke-width:2"/>\n''')
    d = (((vov2 - vov1) ** 2) + ((gog2 - gog1) ** 2)) ** 0.5
    if d == 0:
        continue
    f.write(f'''<line  x1="{xcir + xmin}" y1="{ycir + ymin}" x2="{vov2}" y2="{gog2}" style="stroke:violet;stroke-width:2"/>\n''')
    dd.append(d)
    print(vov2, gog2, '-', vov1, gog2, ' ', d)
    y0 = ycir + ymin
    x0 = xcir + xmin
    delik = (((gog2 - gog1) ** 2) + ((vov2 - vov1) ** 2)) ** 0.5
    h = ((x0 * (gog2 - gog1)) - (y0 * (vov2 - vov1)) + (vov2 * gog1) - (gog2 * vov1)) / delik
    smg = 0.5 * d * h
    summg += smg
otns = ((skv - summg) / skv) * 100
print(dd)
print(skv, summg)
print('Отношение площадей в % -', otns)
if otns > 50:
    print('Это треугольник')
elif otns < 8:
    print('Это круг')
elif otns <= 50:
    print('Это прямоугольник')
f.write(f'''<circle cx="{x0}" cy="{y0}"  r="2" stroke="violet" stroke-width="2"/>\n''')

"""for i in range(len(dd)):
    if dd[i] == 0:
        f.write(f'''<line  x1="{lx}" y1="{375}" x2="{lx}" y2="{400}" style="stroke:rgb(197,208,230);stroke-width:2"/>\n''')
    buk = dd[i]
    f.write(f'''<line  x1="{lx}" y1="{400 - buk}" x2="{lx}" y2="{400}" style="stroke:rgb(255,151,187);stroke-width:2"/>\n''')
    lx += 4"""
f.write('\n</svg>')
f.close
