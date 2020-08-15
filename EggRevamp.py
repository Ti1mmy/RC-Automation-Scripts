"""
Rc-Egg Revamp
------------------------------------------------------------------------------------------------------------------------
Drop rates for the following tiers:
    -Legendary: 5% - 5000 total
    -Ultrabeasts: 10% - 10000 total
    -Extremely Rare: 6% 6000 total
    -Very Rare: 7% - 7000 total
    -Rare: 12% 12000 total
    -Uncommon: 15% 15000 total
    -Common: 20% 20000 total
    -Very Common: 25% 25000 total
------------------------------------------------------------------------------------------------------------------------
TODO:
USE PYPERCLIP TO MAKE COPYING THIS STUFF EASIER
APPEND TO LIST INSTEAD OF PRINT, THEN PRINT FOR I IN LIST
"""

indexnum = 0
legendarypokes = []
ultrabeasts = []
extremelyrarepokes = []
veryrarepokes = []
rarepokes = []
uncommonpokes = []
commonpokes = []
verycommonpokes = []

legendarypokes2 = []
ultrabeasts2 = []
extremelyrarepokes2 = []
veryrarepokes2 = []
rarepokes2 = []
uncommonpokes2 = []
commonpokes2 = []
verycommonpokes2 = []
rarities = [5000, 10000, 6000, 7000, 12000, 15000, 20000, 25000]

print('Legendary: ')
while True:
    to_add = input()
    if to_add == "":
        break
    legendarypokes.append(to_add)

print('Ultrabeasts: ')
while True:
    to_add = input()
    if to_add == "":
        break
    ultrabeasts.append(to_add)

print('Extremelyrarepokes: ')
while True:
    to_add = input()
    if to_add == "":
        break
    extremelyrarepokes.append(to_add)

print('Very Rare Pokes: ')
while True:
    to_add = input()
    if to_add == "":
        break
    veryrarepokes.append(to_add)

print('Rare: ')
while True:
    to_add = input()
    if to_add == "":
        break
    rarepokes.append(to_add)

print('Uncommon: ')
while True:
    to_add = input()
    if to_add == "":
        break
    uncommonpokes.append(to_add)

print('Common: ')
while True:
    to_add = input()
    if to_add == "":
        break
    commonpokes.append(to_add)

print('Very Common: ')
while True:
    to_add = input()
    if to_add == "":
        break
    verycommonpokes.append(to_add)


def pencil(rarenum, poke, legendary, poke2):
    global indexnum
    for str in poke:
        if str not in poke2 or str == "Oricorio" or str == "Floette":
            poke2.append(str)
    for k in range(len(poke2)):
        print(f'            "{indexnum}"', '{')
        print(f'				chance={round(rarities[rarenum] / len(poke2))}')
        print(f'                reward="COMMAND:pokegive %p% {poke2[k]} egg"')
        if legendary:
            print('                message="&l&4&oThis egg is emitting some sort of powerful aura!"')
        print('            }')
        indexnum += 1


print('#Verycommon')
pencil(7, verycommonpokes, False, verycommonpokes2)
print('#Common')
pencil(6, commonpokes, False, commonpokes2)
print('#Uncommon')
pencil(5, uncommonpokes, False, uncommonpokes2)
print('#Rare')
pencil(4, rarepokes, False, rarepokes2)
print('#Veryrare')
pencil(3, veryrarepokes, False, veryrarepokes2)
print('#Extremelyrare')
pencil(2, extremelyrarepokes, False, extremelyrarepokes2)
print('#Ultrabeast')
pencil(1, ultrabeasts, True, ultrabeasts2)
print('#Legendary')
pencil(0, legendarypokes, True, legendarypokes2)
