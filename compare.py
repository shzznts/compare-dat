"""
Created to compare MATLAB output files between folders.

Compares .dat files within a comparing folder against files within a source folder.
Can change EXTENSION to compare a different file extension.

HOW TO:
    1. install python (if not installed)
    2. type "python compare.py SOURCE_PATH COMPARE_PATH" where SOURCE_PATH and COMPARE_PATH
        are the source folder and the comparing folder respectively
    3. glhf
"""
import sys
import os

EXTENSION = '.dat'
if os.name == 'nt':
    DELIMITER = '\\'
else:
    DELIMITER = '/'

source_path = sys.argv[1]
other_path = sys.argv[2]

if not source_path.endswith(DELIMITER):
    source_path += DELIMITER

if not other_path.endswith(DELIMITER):
    other_path += DELIMITER

def compare(source_path=None, other_path=None):
    print('Comparing... %s' % source_path.split(DELIMITER)[-1])
    passed = True
    source = open(source_path, 'r')
    try:
        other = open(other_path, 'r')
    except IOError as e:
        print('*** Unable to find comparing file: %s***' % other_path)
        source.close()
        return False

    for source_line in source:
        other_line = other.readline()
        if not other_line:
            print('*** Reached end of comparing file ***\n')
            passed = False
            break
        else:
            if source_line.strip() != other_line.strip():
                print('Source file: %s' % source_line)
                print('Compare file: %s' % other_line)
                print('*** Mismatch!!! ***\n')
                passed = False
    source.close()
    other.close()
    if passed:
        print('*** Files matched successfully ***')
    return passed

passed = True
for root, dirs, files in os.walk(source_path):
    for file in files:
        if file.endswith(EXTENSION):
            source_file_path = source_path + file
            other_file_path = other_path + file
            if not compare(source_file_path, other_file_path):
                passed = False

if passed:
    print('Success! Files are equivalent!\n')
else:
    print('Failed. Files are NOT equivalent.\n')