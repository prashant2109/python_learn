import zipfile

# with zipfile.ZipFile('files.zip', 'w') as my_zip:
#     my_zip.write('t1.txt')
#     my_zip.write('t2.txt')
#     my_zip.write('hummer.jpg')

with zipfile.ZipFile('l/files.zip') as my_zip:
    my_zip.extractall()
