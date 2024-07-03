import os

directory = 'wiki'

for file in os.scandir(directory):
    if file.is_file() and file.name.lower().endswith('.md'):
        split = file.name.split('-')
        capitalized = [string.capitalize() for string in split]
        new_filename = capitalized[0]
        for string in capitalized[1:]:
            new_filename = new_filename + ' ' + string
        print(new_filename)