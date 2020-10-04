with open("commands.conf", "r", encoding="utf8") as File1:
    lines = File1.read().split('\n')
towrite = []

for line in lines:
    if not line.startswith("#"):
        if "=" in line:
            if f'inventorymenus.cmd.{line.split("=")[0]}' not in towrite:
                towrite.append(f'inventorymenus.cmd.{line.split("=")[0]}')
with open("perms.conf", "a", encoding="utf-8") as output:
    for line in towrite:
        output.write(f'{line}\n')
