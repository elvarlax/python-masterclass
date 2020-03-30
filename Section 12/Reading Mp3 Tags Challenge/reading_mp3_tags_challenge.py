"""
Section 12 Challenge - Reading Mp3 Tags
Create a generator that will return the complete filename of all mp3 files.

The generator should start at a specific directory, the start which will be provided as an
argument to the generator function.

The filenames should include the full path from the specified directory.
So it'll return a relative path.

It's a good idea to make your generator function a bit more generic, so it can handle files with
any extension. So pass the extension as a second parameter to the function.

As an optional extra, you should make the paths absolute - so they specify the filename from the
root of the drive or volume. Check out the documentation for the os module, if you want to do that.

If you haven't got any mp3 files, you can use the music directory from the previous videos,
and search for emp3 files instead.
"""
import os
import fnmatch


def find_music_files(root, extension):
    for path, dirs, files in os.walk(root):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            yield os.path.join(os.path.abspath(path), file)


find_music_files = find_music_files('music', 'emp3')

for i in find_music_files:
    print(i)
