indexnum = 0

common = int(input('Common: '))
extremelyrare = int(input('ExtremelyRare: '))
legendary = int(input('Legendary: '))
rare = int(input('Rare: '))
uncommon = int(input('Uncommon: '))
verycommon = int(input('VeryCommon: '))
veryrare = int(input('VeryRare: '))

legendarypokes = []
extremelyrarepokes = []
veryrarepokes = []
rarepokes = []
uncommonpokes = []
commonpokes = []
verycommonpokes = []
rarities = [22000, 5000, 1000, 13000, 18000, 26000, 10000]

print('Very Common')
verycommonchance = round(rarities[5] / verycommon)
for i in range(verycommon):
    verycommonpokes.append(input())

print('Common')
commonchance = round(rarities[0] / common)
for i in range(common):
    commonpokes.append(input())

print('Uncommon')
uncommonchance = round(rarities[4] / uncommon)
for i in range(uncommon):
    uncommonpokes.append(input())

print('Rare')
rarechance = round(rarities[3] / rare)
for i in range(rare):
    rarepokes.append(input())

print('Very Rare')
veryrarechance = round(rarities[6] / veryrare)
for i in range(veryrare):
    veryrarepokes.append(input())

print('Extremely')
extremelyrarechance = round(rarities[1] / extremelyrare)
for i in range(extremelyrare):
    extremelyrarepokes.append(input())

print('Legendary')
legendarychance = round(rarities[2] / legendary)
for i in range(legendary):
    legendarypokes.append(input())


def pencil(chance, poke, len, shiny, islegendary):
    global indexnum
    if not shiny:
        for k in range(len):
            print(f'            "{indexnum}"', '{')
            print(f'				chance={chance}')
            print(f'                reward="COMMAND:pokegive %p% {poke[k]} egg"')
            if islegendary:
                print('                message="&l&4&oThis egg is emitting some sort of powerful aura!"')
            print('            }')
            indexnum += 1
    else:
        for k in range(len):
            print(f'            "{indexnum}"', '{')
            print(f'				chance={(chance // 20)}')
            print('                message="&6Ooo this egg looks shiny!"')
            print(f'                reward="COMMAND:pokegive %p% {poke[k]} egg s"')
            print('            }')
            indexnum += 1


print('#Verycommon')
pencil(verycommonchance, verycommonpokes, verycommon, False, False)
print('#Common')
pencil(commonchance, commonpokes, common, False, False)
print('#Uncommon')
pencil(uncommonchance, uncommonpokes, uncommon, False, False)
print('#Rare')
pencil(rarechance, rarepokes, rare, False, False)
print('#Veryrare')
pencil(veryrarechance, veryrarepokes, veryrare, False, False)
print('#Extremelyrare')
pencil(extremelyrarechance, extremelyrarepokes, extremelyrare, False, False)
print('#Legendary')
pencil(legendarychance, legendarypokes, legendary, False, True)
print('#Verycommon shiny')
pencil(verycommonchance, verycommonpokes, verycommon, True, False)
print('#Common shiny')
pencil(commonchance, commonpokes, common, True, False)
print('#Uncommon shiny')
pencil(uncommonchance, uncommonpokes, uncommon, True, False)
print('#Rare shiny')
pencil(rarechance, rarepokes, rare, True, False)
print('#Veryrare shiny')
pencil(veryrarechance, veryrarepokes, veryrare, True, False)
print('#Extremelyrare shiny')
pencil(extremelyrarechance, extremelyrarepokes, extremelyrare, True, False)
