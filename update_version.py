import yaml
from pathlib import Path
path = Path(Path.cwd(), ".github", "workflows", "main.yml")
with open(path, "r") as file:
    yml = yaml.safe_load(file)
yml['jobs']['build']['steps'][-1]['with']['version_label'] += 1
with open(path, "w") as file:
    yaml.dump(yml, file)

