import os
with open("names.conf", "r", encoding="utf8") as File1:
    names = File1.read().split('\n')
with open("pokegive.conf", "r", encoding="utf8") as File2:
    commands = File2.read().lower().split('\n')
with open("rarity.conf", "r", encoding="utf8") as File3:
    rarities = File3.read().split('\n')
info = []
weights = []
for filename in os.listdir("Spawning"):
    content = open(os.path.join('Spawning', filename), "r", encoding="utf8")
    contents = content.read().split('\n')
    for line in contents:
        if '"rarity"' in line:
            weights.append([int((float(line.split(": ")[1]) * 10)), filename.split(".")[0]])
for weight in weights:
    print(weight)
for i in range(len(names)):
    info.append([names[i], commands[i], rarities[i]])

# for thing in info:
#     print(thing)
final_list = []
print(commands.index("zeraora"))
last_poke = ""
for poke in weights:
    print(poke[1])
    if poke[1] != last_poke:
        final_list.append([poke[1], names[commands.index(poke[1].lower())], rarities[commands.index(poke[1].lower())], poke[0]])
    else:
        final_list[-1][-1] += poke[0]
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
total_odds = 0
for poke in final_list:
    if "Legendary" in poke:
        legendary.append(poke)
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
pool.append("        # StartLegendary_&6")
for poke in legendary:
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-1]}')
    pool.append(f'                reward="COMMAND:pokespawncoords {poke[0]} %p%"')
    if poke[1][0].lower() in ['a', 'e', 'i', 'o', 'u']:
        pool.append(f'                message="&bAn &6{poke[1]} &bpopped out of the ball!"')
    else:
        pool.append(f'                message="&bA &6{poke[1]} &bpopped out of the ball!"')
    pool.append('            }')
    index += 1
pool.append("        # StartUltraRare_&5")
for poke in ultra_rare:
    total_odds += poke[-1]
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-1]}')
    pool.append(f'                reward="COMMAND:pokespawncoords {poke[0]} %p%"')
    if poke[1][0].lower() in ['a', 'e', 'i', 'o', 'u']:
        pool.append(f'                message="&bAn &5{poke[1]} &bpopped out of the ball!"')
    else:
        pool.append(f'                message="&bA &5{poke[1]} &bpopped out of the ball!"')
    pool.append('            }')
    index += 1
pool.append("        # StartVeryRare_&9")
for poke in very_rare:
    total_odds += poke[-1]
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-1]}')
    pool.append(f'                reward="COMMAND:pokespawncoords {poke[0]} %p%"')
    if poke[1][0].lower() in ['a', 'e', 'i', 'o', 'u']:
        pool.append(f'                message="&bAn &9{poke[1]} &bpopped out of the ball!"')
    else:
        pool.append(f'                message="&bA &9{poke[1]} &bpopped out of the ball!"')
    pool.append('            }')
    index += 1
pool.append("        # StartRare_&2")
for poke in rare:
    total_odds += poke[-1]
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-1]}')
    pool.append(f'                reward="COMMAND:pokespawncoords {poke[0]} %p%"')
    if poke[1][0].lower() in ['a', 'e', 'i', 'o', 'u']:
        pool.append(f'                message="&bAn &2{poke[1]} &bpopped out of the ball!"')
    else:
        pool.append(f'                message="&bA &2{poke[1]} &bpopped out of the ball!"')
    pool.append('            }')
    index += 1
pool.append("        # StartUncommon_&2")
for poke in uncommon:
    total_odds += poke[-1]
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-1]}')
    pool.append(f'                reward="COMMAND:pokespawncoords {poke[0]} %p%"')
    if poke[1][0].lower() in ['a', 'e', 'i', 'o', 'u']:
        pool.append(f'                message="&bAn &2{poke[1]} &bpopped out of the ball!"')
    else:
        pool.append(f'                message="&bA &2{poke[1]} &bpopped out of the ball!"')
    pool.append('            }')
    index += 1
pool.append("        # StartCommon_&7")
for poke in common:
    total_odds += poke[-1]
    pool.append(f'            "{index}" ' + '{')
    pool.append(f'                chance={poke[-1]}')
    pool.append(f'                reward="COMMAND:pokespawncoords {poke[0]} %p%"')
    if poke[1][0].lower() in ['a', 'e', 'i', 'o', 'u']:
        pool.append(f'                message="&bAn &7{poke[1]} &bpopped out of the ball!"')
    else:
        pool.append(f'                message="&bA &7{poke[1]} &bpopped out of the ball!"')
    pool.append('            }')
    index += 1
pool.append("        }")
with open("output.conf", "a", encoding="utf-8") as output:
    for line in pool:
        output.write(f'{line}\n')
print(total_odds)