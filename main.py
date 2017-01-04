import os
import sys
import glob

if __name__ == '__main__':
    proj = sys.argv[1]
    path = proj + '/app/controllers'
    query = sys.argv[2]
    for filename in glob.glob(os.path.join(path, '*.rb')):
        with open(filename, 'r') as f:
            if query in f.read():
                print(filename)

#write recursive folder traversal
