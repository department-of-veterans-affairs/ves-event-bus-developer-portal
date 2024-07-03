import os

directory = 'wiki'

for file in os.scandir(directory):
    if file.is_file() and file.name.lower().endswith((".md")):
        new_filename = file.name.replace("-", " ").title()
        print(new_filename)