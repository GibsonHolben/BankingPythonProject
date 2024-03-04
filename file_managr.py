import os
import shutil
import Variables as v

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


def save_data():
    """Saves all the data of the program"""
    to_save = ''
    for x in v.names:
        to_save = to_save + x + ','
    to_save = to_save.strip(',')
    write_file(v.home + '/Documents/PythonBank/names.bank', to_save)

    to_save = ''
    for x in v.passwords:
        to_save = to_save + x + ','
    to_save = to_save.strip(',')
    write_file(v.home + '/Documents/PythonBank/pass.bank', to_save)

    to_save = ''
    for x in v.balance:
        to_save = to_save + x + ','
    to_save = to_save.strip(',')
    write_file(v.home + '/Documents/PythonBank/bal.bank', to_save)