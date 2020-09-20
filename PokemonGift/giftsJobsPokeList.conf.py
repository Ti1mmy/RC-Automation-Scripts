import os
with open("names.conf", "r", encoding="utf8") as File1:
    names = File1.read().split('\n')
with open("pokegive.conf", "r", encoding="utf8") as File2:
    commands = File2.read().lower().split('\n')
with open("rarity.conf", "r", encoding="utf8") as File3:
    rarities = File3.read().split('\n')
with open("types.txt", "r", encoding="utf8") as File4:
    types = File4.read().split('\n')
info = []
weights = []
total_odds = 0
for filename in os.listdir("Spawning"):
    content = open(os.path.join('Spawning', filename), "r", encoding="utf8")
    contents = content.read().split('\n')
    for line in contents:
        if filename.split(".")[0].lower() in commands:
            if '"rarity"' in line:
                weights.append([int((float(line.split(": ")[1]) * 10)), filename.split(".")[0]])
for i in range(len(names)):
    info.append([names[i], commands[i], rarities[i], types[i]])

# for thing in info:
#     print(thing)
final_list = []
last_poke = ""
for poke in weights:
    print(poke[1])
    if poke[1] != last_poke:
        final_list.append([poke[1], names[commands.index(poke[1].lower())], rarities[commands.index(poke[1].lower())], poke[0], types[commands.index(poke[1].lower())]])
    else:
        final_list[-1][-2] += poke[0]
    last_poke = poke[1]
print(final_list)
pool = []
index = 0
legendary = []
ultra_rare = []
very_rare = []
rare = []
uncommon = []
common = []
for poke in final_list:
    if "Ground" in poke[4] or "Rock" in poke[4]:
        if "Legendary" in poke:
            # legendary.append(poke)
            pass
        elif "Ultra Rare" in poke:
            ultra_rare.append(poke)
        elif "Very Rare" in poke:
            very_rare.append(poke)
        elif "Rare" in poke:
            rare.append(poke)
        elif "Uncommon" in poke:
            uncommon.append(poke)
        elif "Common" in poke:
            common.append(poke)

pool.append('        randomspawn {')
# pool.append("        # StartLegendary")
# for poke in legendary:
#     pool.append(f'            "{index}" ' + '{')
#     pool.append(f'                chance={poke[-2]}')
#     pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]}"')
#     pool.append('            }')
#     index += 1
pool.append("        # StartUltraRare")
for poke in ultra_rare:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2] * 20}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]}"')
    pool.append('            }')
    index += 1
pool.append("        # StartVeryRare")
for poke in very_rare:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2] * 20}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]}"')
    pool.append('            }')
    index += 1
pool.append("        # StartRare")
for poke in rare:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2] * 20}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]}"')
    pool.append('            }')
    index += 1
pool.append("        # StartUncommon")
for poke in uncommon:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2] * 20}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]}"')
    pool.append('            }')
    index += 1
pool.append("        # StartCommon")
for poke in common:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2] * 20}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]}"')
    pool.append('            }')
    index += 1
# Shiny
pool.append("        # StartUltraRare_S")
for poke in ultra_rare:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2]}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]} shiny"')
    pool.append('            }')
    index += 1
pool.append("        # StartVeryRare_S")
for poke in very_rare:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2]}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]} shiny"')
    pool.append('            }')
    index += 1
pool.append("        # StartRare")
for poke in rare:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2]}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]} shiny"')
    pool.append('            }')
    index += 1
pool.append("        # StartUncommon_S")
for poke in uncommon:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2]}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]} shiny"')
    pool.append('            }')
    index += 1
pool.append("        # StartCommon_S")
for poke in common:
    total_odds += poke[-2] * 20
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-2]}')
    pool.append(f'                reward="COMMAND:pokemonbattle %p% {poke[0]} shiny"')
    pool.append('            }')
    index += 1
pool.append("        }")
with open("output.conf", "a", encoding="utf-8") as output:
    for line in pool:
        output.write(f'{line}\n')
print(total_odds)