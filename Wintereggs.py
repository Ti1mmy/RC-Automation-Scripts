"""
list = []
newlist = []
newnewlist = ['Snorunt', 'Glaceon', 'Vanillite', 'Cubchoo', 'Cryogonal', 'Vulpix', 'Bergmite', 'Swinub', 'Delibird', 'Smoochum', 'Spheal', 'Shellder', 'Sneasel', 'Snover', 'Stantler', 'Deerling', 'Squirtle', 'Piplup', 'Lapras', 'Amaura', 'Castform', 'Litwick', 'Pineco', 'Togepi', 'Baltoy', 'Staryu', 'Azurill', 'Clamperl', 'Ducklett', 'Teddiursa', 'MimeJr', 'Munchlax', 'Seel', 'Chingling', 'Skitty', 'Swablu', 'Zubat', 'Goldeen', 'Jirachi', 'Jirachi"', 'Suicune', 'Suicune"', 'Articuno', 'Articuno"', 'Regice', 'Regice"', 'Lugia', 'Lugia"', 'Kyurem', 'Kyurem"', 'Regigigas', 'Regigigas"']
while True:
    a = input()
    if a == "":
        break
    else:
        list.append(a)

for i in range(len(list)):
    if "pokegive" in list[i] and list[i] not in newlist:
        newlist.append(list[i])
for i in range(len(newlist)):
    newlist[i] = newlist[i].strip()
    c = newlist[i].split()[2]
    if c not in newnewlist:
        newnewlist.append(c)
for text in newnewlist:
    print(text)
"""

pokemon = []
indexnum = 0
while True:
    a = input()
    if a == "":
        break
    else:
        pokemon.append(a)

def pencil():


