import yaml
import sys
from pprint import pprint

# variables/counters declaration
in_yaml = False
content = []
counter = 0

filename = sys.argv[1]

# Read input file
with open(filename, 'r') as f:
    lines = f.readlines()

all_lines = []
for line in lines:
    all_lines.append(line.replace("\n",""))

lines = all_lines

# print(lines)

# Loop through all the lines
for line in lines:
    counter = counter + 1

    if not in_yaml and line.startswith('```'):
        in_yaml = True
    elif in_yaml and line.startswith("```"):
        in_yaml = False
    elif in_yaml:
        content.append(line)

s = '\n'.join(content)

try:

    d = yaml.load(s)
    print("The file is in a valid yaml format")

except Exception as e:
    print ("ERROR: The file is not in a valid yaml format")
