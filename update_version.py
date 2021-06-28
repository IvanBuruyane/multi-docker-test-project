import re
from pathlib import Path

path = Path(Path.cwd(), ".github", "workflows", "main.yml")
with open(path, "r") as file:
    yml = file.read()

find = re.search(r"version_label:\s*(\d)+\s*\n", yml).group(0)
n = int(re.search(r"\d+", find).group(0))
n += 1
new_string = f"version_label: {n}\n"
new_yml = re.sub(r"version_label:\s*(\d)+\s*\n", new_string, yml)
with open(path, "w") as file:
    file.write(new_yml)

