import sys
from pathlib import Path

from tabulate import tabulate
import toml
import os

dir_path = Path(os.getcwd())
if len(sys.argv) > 1:
    dir_path = Path(sys.argv[1])

    if not dir_path.is_dir():
        print("Given path, %s, is not a path" % dir_path.absolute())

files = os.listdir(dir_path)

file_meta = {}
simple_files = []
dirs = []
# Let's get all meta.toml-files

print("\nhyBit Metadata Directory Listing")
print("Path: %s" % dir_path.resolve())
print()


# For now keep it simple: One meta per file (or no)
def parse_toml(filename, dir):
    path = Path(dir).joinpath(filename)
    toml_data = toml.load(path)
    if filename == '.metadata.toml':
        if 'files' in toml_data['meta']:
            for file in toml_data['meta']['files']:
                file_meta[file] = {
                    'owner': '%s <%s>' % (toml_data['owner']['name'], toml_data['owner']['contact']),
                    'access': toml_data['meta']['access']
                }

    else:
        filename = filename[:-14]
        file_meta[filename] = {
            'owner': '%s <%s>' % (toml_data['owner']['name'], toml_data['owner']['contact']),
            'access': toml_data['meta']['access']
        }


for file in files:
    file_path = Path(dir_path).joinpath(file)
    if os.path.isdir(file_path):
        dirs.append(file)
        continue

    if file.endswith('metadata.toml'):
        parse_toml(file, dir_path)
    else:
        simple_files.append(file)

file_data = []

if '*' in file_meta:
    file_data.append(['* hyBit Ordnerrechte *', file_meta['*']['access'], file_meta['*']['owner']])

for file in sorted(simple_files):
    if file in file_meta:
        file_data.append([file, file_meta[file]['access'], file_meta[file]['owner']])
    elif '*' in file_meta:
        file_data.append([file, file_meta['*']['access'], file_meta['*']['owner']])
    else:
        file_data.append([file, 'offen', '? / nicht definiert'])

if len(dirs) > 0:
    print("Ordner")
    for folder in dirs:
        print(folder)
    print()

if len(simple_files) > 0:
    print(tabulate(file_data, headers=['Datei', 'Zugriff', 'Kontakt']))