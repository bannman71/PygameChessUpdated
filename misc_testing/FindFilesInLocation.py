from os import walk
f = []
for (dirpath, dirnames, filenames) in walk(r'/Users/maxscullion/Projects/PygameChess'):
    f.extend(filenames)
    break
