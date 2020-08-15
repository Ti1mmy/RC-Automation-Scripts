"""
Battle-Ready Mons Configurator pt.2
------------------------------------------------------------------------------------------------------------------------
4 Sets are possible for each poke, all being pretty useless barring the main set.
Chances =
    -Normal1: 9
    -Normal2: 9
    -HA1: 1
    -HA2: 1

Pokemon positions:
    0: Normal Ability 5/6 150
    1: Normal Ability 6/6 25
    2: Hidden Ability 5/6 15
    3: Hidden Ability 6/6 5
    4: Normal Ability 6/6 Shiny 2
    5: Hidden Ability 6/6 Shiny 1
------------------------------------------------------------------------------------------------------------------------
"""
indexnum = 0
pokemon = []
pokemonnamenotfinal = []

print('Copy-Paste commands: ')
while True:
    to_add = input()
    if to_add == "":
        break
    pokemon.append(to_add)

for l in range(len(pokemon)):
    thing = pokemon[l].split()
    if "f:1" in pokemon[l]:
        pokemonnamenotfinal.append(str("Alolan" + thing[2]))
    else:
        pokemonnamenotfinal.append(thing[2])


for k in range(len(pokemon)):
    if indexnum % 6 == 0:
        print(f'            "{indexnum}"', '{')
        print('				chance=150')
        print(f'                reward={pokemon[k]}')
        print(f'                message="&bCongrats on the &25/6 Battle-Ready {pokemonnamenotfinal[indexnum]}&b!"')
        print('            }')
    elif indexnum % 6 == 2:
        print(f'            "{indexnum}"', '{')
        print('				chance=15')
        print(f'                reward={pokemon[k]}')
        print(f'                message="&bCongrats on the &95/6 H/A Battle-Ready {pokemonnamenotfinal[indexnum]}&b!"')
        print('            }')
    elif indexnum % 6 == 1:
        print(f'            "{indexnum}"', '{')
        print('				chance=25')
        print(f'				reward={pokemon[k]}')
        print(f'				message="&bCongrats on the &56/6 Battle-Ready {pokemonnamenotfinal[indexnum]}&b!"')
        print('            }')
    elif indexnum % 6 == 3:
        print(f'            "{indexnum}"', '{')
        print('				chance=5')
        print(f'				reward={pokemon[k]}')
        print(f'				message="&bCongrats on the &56/6 H/A Battle-Ready {pokemonnamenotfinal[indexnum]}&b!"')
        print('            }')
    elif indexnum % 6 == 4:
        print(f'            "{indexnum}"', '{')
        print('				chance=2')
        print(f'				reward={pokemon[k]}')
        print(f'				message="&bCongrats on the &6Shiny 6/6 Battle-Ready {pokemonnamenotfinal[indexnum]}&b!"')
        print('            }')
    elif indexnum % 6 == 5:
        print(f'            "{indexnum}"', '{')
        print('				chance=1')
        print(f'				reward={pokemon[k]}')
        print(f'				message="&bCongrats on the &6Shiny 6/6 H/A Battle-Ready {pokemonnamenotfinal[indexnum]}&b!"')
        print('            }')
    indexnum += 1