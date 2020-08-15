pokemon = []
pokemon2 = []

while True:
    to_add = input()
    if to_add == "":
        break
    pokemon.append(to_add)

for k in range(len(pokemon)):
    thing = pokemon[k].split()
    if "f:1" in pokemon[k]:
        pokemon2.append(str(thing[2] + "(Alolan)"))
    else:
        pokemon2.append(thing[2])
final = []
for str in pokemon2:
    if str not in final:
        final.append(str)
for i in range(len(final)):
    print(final[i])



