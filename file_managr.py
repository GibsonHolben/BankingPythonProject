import os
import shutil


def rem_file(path):
    """Removes the specified file"""
    try:
        if os.path.isfile(path):
            os.remove(path)
    except Exception as e:
        print(e)


def rem_dir(path):
    """Removes the specified file"""
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            print('not a dir')
    except:
        print('could not remove the directory at: ' + path)


def read_file(path):
    """Reads the contents of a specified path"""
    try:
        if os.path.isfile(path):
            file = open(path, 'r')
            var = file.read()
            file.close()
            return var

        else:
            file = open(path, 'w+')
            file.close()
            file = open(path, 'r')

            return file.read()
    except:
        print('could not read the file at: ' + path)


def write_file(path, contents):
    """Writes to the specified file with the specified contents"""
    try:
        file = open(path, 'w')
        file.write(contents)
    except:
        print('could not write to the file at: ' + path)

