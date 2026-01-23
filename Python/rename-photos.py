import os

folder = 'C:/Users/RComperchio27/Documents/377-web-app-dev/Photos'
prefix = 'Dog'
count = 1
file_type = 'jpg'

for filename in os.listdir(folder):
    extension = filename.split('.')[-1]
    if extension == file_type:
        new_filename = prefix + '-' + str(count) + '.' + file_type

        source = folder + '/' + filename
        destination = folder + '/' + new_filename

        print('Renaming ' + filename + ' to ' + new_filename)
        os.rename(source, destination) # source is old file, destination is new name
        count += 1 
