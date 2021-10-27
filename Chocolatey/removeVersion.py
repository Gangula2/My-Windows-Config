# run code in terminal "cd Chocolatey & python removeVersion.py"

import os, re

filename = "packages.config"
editedFilename = filename.replace(".config", " - noVersions.config")

dir_path = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(dir_path, filename)
editedFilePath = os.path.join(dir_path, editedFilename)

pattern = re.compile(r"(^\s.*)(\sversion.*)( \/>)")

with open(filepath, "r", encoding="utf-8") as file:
    data = file.readlines()

editedData = []
for line in data:
    editedData.append(re.sub(pattern, r"\1\3", line))

with open(editedFilePath, mode="wt", encoding="utf-8") as f:
    f.write("".join(editedData))
