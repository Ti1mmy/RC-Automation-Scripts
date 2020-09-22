with open("commands.conf", "r", encoding="utf8") as File1:
    lines = File1.read().split('\n')
write = []
for line in lines:
    if not line.startswith("#"):
        if "=" in line:
            if f'inventorymenus.cmd.{line.split("=")[1]}' not in write:
                write.append(f'inventorymenus.cmd.{line.split("=")[1]}')
with open("output.conf", "a", encoding="utf-8") as output:
    for line in write:
        output.write(f'{line}\n')