indexnum = 0

common = int(input('Common: '))
uncommon = int(input('Uncommon: '))
rare = int(input('Rare: '))
veryrare = int(input('VeryRare: '))
extremelyrare = int(input('ExtremelyRare: '))
legendary = int(input('Legendary: '))

commonpokes = []
uncommonpokes = []
rarepokes = []
veryrarepokes = []
extremelyrarepokes = []
legendarypokes = []
rarities = [6000, 5000, 4000, 3000, 2000, 1000]

if common != 0:
    print('Common')
    commonchance = round(rarities[0] / common)
    for i in range(common):
        commonpokes.append(input())
if uncommon != 0:
    print('Uncommon')
    uncommonchance = round(rarities[1] / uncommon)
    for i in range(uncommon):
        uncommonpokes.append(input())
if rare != 0:
    print('Rare')
    rarechance = round(rarities[2] / rare)
    for i in range(rare):
        rarepokes.append(input())
if veryrare != 0:
    print('Very Rare')
    veryrarechance = round(rarities[3] / veryrare)
    for i in range(veryrare):
        veryrarepokes.append(input())
if extremelyrare != 0:
    print('Extremely')
    extremelyrarechance = round(rarities[4] / extremelyrare)
    for i in range(extremelyrare):
        extremelyrarepokes.append(input())
if legendary != 0:
    print('Legendary')
    legendarychance = round(rarities[5] / legendary)
    for i in range(legendary):
        legendarypokes.append(input())


def pencil(chance, poke, len):
    global indexnum
    if True:
        for k in range(len):
            print(f'            "{indexnum}"', '{')
            print(f'				chance={chance}')
            print(f'                reward="ITEM:pixelmon:{poke[k]}:0:1"')
            print('            }')
            indexnum += 1


if common != 0:
    print('#Common')
    pencil(commonchance, commonpokes, common)
if uncommon != 0:
    print('#Uncommon')
    pencil(uncommonchance, uncommonpokes, uncommon)
if rare != 0:
    print('#Rare')
    pencil(rarechance, rarepokes, rare)
if veryrare != 0:
    print('#Veryrare')
    pencil(veryrarechance, veryrarepokes, veryrare)
if extremelyrare != 0:
    print('#Extremelyrare')
    pencil(extremelyrarechance, extremelyrarepokes, extremelyrare)
if legendary != 0:
    print('#Legendary')
    pencil(legendarychance, legendarypokes, legendary)
