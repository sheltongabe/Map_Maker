"""fileio.py
    handle the input and output for files fot he map-kamer
"""

from tile import Tile;
from gameobject import GameObject;

class FileIO(object):

    def __init__(self):
        pass;

    @classmethod
    def load(self, path):
        f = open(path, 'r');
        line = f.readline();
        line = line.split(' ');

        print(line);
        num_cols = line[1];
        num_rows = line[2];
        x_offset = int(line[3]);
        y_offset = int(line[4]);

        tiles = [];

        for i in range(0, int(num_rows)):
            tiles.append([]);
            for j in range(0, int(num_cols)):
                line = f.readline().split(' ');
                tile = Tile(line[0],
                            x = int(line[1]),
                            y = int(line[2]));
                tile.in_bin = False;
                tiles[i].append(tile);
            #end of row
            f.readline();

        #end of line
        f.readline();

        #GameObject header
        f.readline();

        objects = [];
        for line in f:
            line = line.split(' ');
            item = GameObject(line[0]);
            item.rect.x = int(line[1]);
            item.rect.y = int(line[2]);
            item.in_bin = False;
            objects.append(item);

        f.close();
        return (tiles, objects, x_offset, y_offset);



    @classmethod
    def save(self, path, data):
        tiles = data[0];
        objects = data[1];
        x_offset = data[2];
        y_offset = data[3];

        output = '';

        #add tiles header
        output += 'Tiles {} {} {} {}\n'.format(len(tiles[0]),
                                             len(tiles),
                                             x_offset,
                                             y_offset);

        for i, row in enumerate(tiles):
            for j, item in enumerate(row):
                output += '{} {} {}\n'.format(item.path,
                                                  item.rect.x,
                                                  item.rect.y);
            #new line to show end of row
            output += '\n';

        #new line to show end of tiles
        output += '\n';

        #GameObject header
        output += 'GameObject\n';

        for item in objects:
            output += '{} {} {} {} {}\n'.format(item.path,
                                              item.rect.x,
                                              item.rect.y,
                                              item.rect.width,
                                              item.rect.height);

        #create file stream
        f = open(path, 'w');
        f.write(output);
        f.close();


