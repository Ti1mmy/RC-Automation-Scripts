"""
To anyone reading this, fist and foremost, sorry.

Ok now that's over with,
-------------------------------------------------------------------------------
Type Egg rarity calc v2.0 - Timmy
-------------------------------------------------------------------------------
Legendary = 1
ExtremelyRare = 5
VeryRare = 10
Rare = 13
Uncommon = 18
Common = 22
VeryCommon = 26

All rarities multiplied by 1000 to improve accuracy, espeicially for higher
rarities without the use of decimals.
"""

common = int(input('Common: '))
extremelyrare = int(input('ExtremelyRare: '))
legendary = int(input('Legendary: '))
rare = int(input('Rare: '))
uncommon = int(input('Uncommon: '))
verycommon = int(input('VeryCommon: '))
veryrare = int(input('VeryRare: '))


rare = [common, extremelyrare, legendary, rare, uncommon, verycommon, veryrare]
rarities = [22000, 5000, 1000, 13000, 18000, 26000, 10000]
for i in range(len(rare)):
    print(round(rarities[i] / rare[i]))


