import re


line = input()

line_spaceless = re.sub(r"/|\s", "", line)

# line_spaceless = line.replace("_", "").replace(" ", "")

print("".join(line_spaceless))
