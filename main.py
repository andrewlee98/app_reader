import os
import sys
import glob

def views_search(query, view_path):
    for cur, _dirs, files in os.walk(view_path):
        for dir in _dirs:
            views_search(query, dir)
        for file in files:
            f = open(cur + '/' + file)
            if query in f.read():
               print(cur + '/' + file)

if __name__ == '__main__':
    proj = sys.argv[1]
    path = proj + '/app/views/'
    query = sys.argv[2]
    views_search(query, path)

