import os

directory = 'wiki'

for file in os.scandir(directory):
    if file.is_file() and file.name.lower().endswith(('.md')):
        print(file.name)