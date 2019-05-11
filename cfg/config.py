from os import getcwd as osg
from os.path import join as opj

## Folder paths
paths = {
    'default': osg(),
    'db': opj(osg(), 'db'),
    'valid': opj(osg(), 'db', 'valid'),
    'train': opj(osg(), 'db', 'train'),
    'test': opj(osg(), 'db', 'test'),
}

path_db = {
    'pistol' : opj(paths['default'], 'data'),
    'others' : opj(paths['default'], 'BK4'),
}

## File types
file_types = {
    'img' : '.jpg',
    'txt' : '.txt',
    'xml' : '.xml',
}

## Param
params = {
    'valid' : 0.2,
    'train' : 0.8,
    'test' : 0
}