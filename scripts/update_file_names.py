import os

directory = 'wiki'

for file in os.scandir(directory):
    if file.is_file() and file.name.lower().endswith('.md'):
        filename = file.name
        split = file.name.split('-')
        capitalized = [string.capitalize() for string in split]
        new_filename = directory + '/' + capitalized[0]
        for string in capitalized[1:]:
            new_filename = new_filename + ' ' + string
        os.rename(file.path, new_filename)