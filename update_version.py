import os
from pathlib import Path

path = Path(Path.cwd(), "version.txt")
print(path)

with open(path, "r") as file:
    text = file.read()

version = int(text)
version += 1
os.environ["VERSION_LABEL"] = f"{version}"
print("Environment version label: " + os.environ.get("VERSION_LABEL"))
print(os.environ)
with open(path, "w") as file:
    file.write(str(version))

