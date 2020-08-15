"""
Battle-Ready Mons Configurator
------------------------------------------------------------------------------------------------------------------------
4 Sets are possible for each poke, all being pretty useless barring the main set.
Chances =
    -Normal1: 9
    -Normal2: 9
    -HA1: 1
    -HA2: 1
"""

pokemonname = input("Pokemon Name: ")
missingiv = input("Missing iv? (hp, def, spatk, spdef, spd, atk) ")
ability = input("Ability? ")
hiddenability = input("Hidden Ability? ")
nature = input("Nature? ")
ivs = ["ivhp:31 ", "ivattack:31 ", "ivdefence:31 ", "ivspecialattack:31 ", "ivspecialdefence:31 ", "ivspeed:31 "]
ivs66 = ["ivhp:31 ", "ivattack:31 ", "ivdefence:31 ", "ivspecialattack:31 ", "ivspecialdefence:31 ", "ivspeed:31 "]
ivnames = ["hp", "atk", "def", "spatk", "spdef", "spd"]
for i in range(len(ivs)):
    if missingiv == ivnames[i]:
        ivs[i] = ""

print(f'"COMMAND:pokegive %p% {pokemonname} {ivs[0]}{ivs[1]}{ivs[2]}{ivs[3]}{ivs[4]}{ivs[5]}nature:{nature} ability:{ability} unbreedable"')
print(f'"COMMAND:pokegive %p% {pokemonname} {ivs66[0]}{ivs66[1]}{ivs66[2]}{ivs66[3]}{ivs66[4]}{ivs66[5]}nature:{nature} ability:{ability} unbreedable"')
print(f'"COMMAND:pokegive %p% {pokemonname} {ivs[0]}{ivs[1]}{ivs[2]}{ivs[3]}{ivs[4]}{ivs[5]}nature:{nature} ability:{hiddenability} unbreedable"')
print(f'"COMMAND:pokegive %p% {pokemonname} {ivs66[0]}{ivs66[1]}{ivs66[2]}{ivs66[3]}{ivs66[4]}{ivs66[5]}nature:{nature} ability:{hiddenability} unbreedable"')
print(f'"COMMAND:pokegive %p% {pokemonname} {ivs66[0]}{ivs66[1]}{ivs66[2]}{ivs66[3]}{ivs66[4]}{ivs66[5]}nature:{nature} ability:{ability} unbreedable s"')
print(f'"COMMAND:pokegive %p% {pokemonname} {ivs66[0]}{ivs66[1]}{ivs66[2]}{ivs66[3]}{ivs66[4]}{ivs66[5]}nature:{nature} ability:{hiddenability} unbreedable s"')