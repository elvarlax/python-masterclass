"""
Section 12 Challenge - Id3reader
Modify the program to handle any exceptions that are raised by the id3reader module.

If an exception is found, record the filename in a list, and move on to the next file.

Once the loop finishes, print out all the files that caused an error.
"""
import os
import fnmatch
import id3reader_p3 as id3reader


def find_music_files(root, extension):
    for path, dirs, files in os.walk(root):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            yield os.path.join(os.path.abspath(path), file)


find_music_files = find_music_files('music', 'emp3')

exception_list = []

for i in find_music_files:
    try:
        id3r = id3reader.Reader(i)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title'),
        ))
    except Exception:
        exception_list.append(i)

for i in exception_list:
    print(i)
